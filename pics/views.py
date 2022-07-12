from django.contrib import messages
from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.forms import ModelForm
from django.forms import modelformset_factory
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from datetime import date, timedelta
from puppy_pics.forms import NewUserForm
from puppy_pics.models import PuppyPic, Pet


# Create your views here.
def puppy_pic_view(request):
    ImageFormSet = modelformset_factory(PuppyPic, form=PhotoForm)  # , extra=3

    context = dict(photo_form=PhotoForm())
    context["dataset"] = PuppyPic.objects.all().order_by("-id")
    context["pet_form"] = PetForm()
    context["formset"] = ImageFormSet(queryset=PuppyPic.objects.none())
    context["todays_date"] = date.today()
    if request.method == 'POST':
        pet_form = PetForm(request.POST)
        formset = ImageFormSet(request.POST, request.FILES)
        if pet_form.is_valid() and formset.is_valid():
            # print("CLEANED DATA, ", pet_form.cleaned_data['name'])
            if Pet.objects.filter(name=pet_form.cleaned_data[
                'name'].capitalize()):  # if the pet is already there, just select that pet

                for form in formset.cleaned_data:
                    if form:
                        image = form['img']
                        name = form['name']
                        description = form['description']
                        # added_by = form['added_by']

                        PuppyPic.objects.create(img=image,
                                                pet=Pet.objects.filter(name=pet_form.cleaned_data['name'].capitalize())[
                                                    0], name=name, description=description, added_by=request.user, )
            else:
                pet_obj = pet_form.save()  # else add the pet

                for form in formset.cleaned_data:
                    if form:
                        image = form['img']
                        name = form['name']
                        description = form['description']
                        # added_by = form['added_by']

                        PuppyPic.objects.create(img=image, pet=pet_obj, name=name, description=description,
                                                added_by=request.user, )
        return redirect('upload')

    return render(request, 'upload.html', context)


class PhotoForm(ModelForm):
    class Meta:
        model = PuppyPic
        # fields = '__all__'
        exclude = ('date_added', 'pet', 'added_by')  # , 'added_by'
        labels = {'name': 'Title of Photo', 'img': 'Image'}
        help_texts = {'description': 'Something short, sweet, and fun', }


class DateInput(forms.DateInput):  # widget for date selector
    input_type = "date"

    def __init__(self, **kwargs):
        kwargs["format"] = "%Y-%m-%d"
        # kwargs["format"] = "%d-%m-%Y"
        super().__init__(**kwargs)


class PetForm(ModelForm):
    class Meta:
        model = Pet
        fields = '__all__'
        labels = {'name': 'Name of Pet'}
        widgets = {'born': DateInput(format=["%Y-%m-%d"], ),

        }
        help_texts = {'born': 'If the pet is already added, skip this',
            'description': 'Something short, sweet, and fun', }


def register_request(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful.")
            return redirect("login")
        messages.error(request, "Unsuccessful registration. Invalid information.")
    form = NewUserForm()
    return render(request=request, template_name="register.html", context={"register_form": form})


def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect("upload")
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request=request, template_name="login.html", context={"login_form": form})


def logout_request(request):
    logout(request)
    messages.info(request, "You have successfully logged out.")
    return redirect("upload")


def documentation(request):
    context = dict(current_user=request.user)
    return render(request, 'documentation.html', context)
