from django.contrib import messages
from django.shortcuts import render, redirect
from django.views.generic import UpdateView
from django.forms import ModelForm
from django.forms import modelformset_factory
from django import forms
from django.contrib.auth import login, logout, authenticate
from datetime import date
from puppy_pics.forms import NewUserForm, UserLoginForm
from puppy_pics.models import PuppyPic, Pet
from django.core.mail import send_mail
from django.conf import settings


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
            if Pet.objects.filter(name=pet_form.cleaned_data['name'].capitalize()):  # if the pet is already there, just select that pet
                for form in formset.cleaned_data:
                    if form:
                        image = form['img']
                        name = form['name']
                        description = form['description']
                        # added_by = form['added_by']

                        PuppyPic.objects.create(img=image,
                                                pet=Pet.objects.filter(name=pet_form.cleaned_data['name'].capitalize())[
                                                    0], name=name, description=description, added_by=request.user, )
                        send_email(name, request.user)

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
                        send_email(name, request.user)

        return redirect('upload')
    # print(request.user.email)
    return render(request, 'upload.html', context)


class PhotoForm(ModelForm):
    class Meta:
        model = PuppyPic
        # fields = '__all__'
        exclude = ('date_added', 'pet', 'added_by')  # , 'added_by'
        labels = {'name': 'Title of Photo', 'img': 'Image'}
        help_texts = {
            'description': 'Something short, sweet, and fun',
            'name': 'What is the title of the photo?',

        }


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
        widgets = {'born': DateInput(format=["%Y-%m-%d"], )}

        help_texts = {
            'breed': 'Skip this if the pet is already added',
            'born': 'Skip this if the pet is already added',
            'owner': 'Skip this if the pet is already added',
            'description': 'Something short, sweet, and fun',
        }


def register_request(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful.")
            return redirect("upload")
        messages.error(request, "Unsuccessful registration. Invalid information.")
    form = NewUserForm()
    return render(request=request, template_name="register.html", context={"register_form": form})


def login_request(request):
    if request.method == "POST":
        form = UserLoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            username = username.lower()
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
    form = UserLoginForm()
    return render(request=request, template_name="login.html", context={"login_form": form})


def logout_request(request):
    logout(request)
    messages.info(request, "You have successfully logged out.")
    return redirect("upload")


def documentation(request):
    context = dict(current_user=request.user)
    return render(request, 'documentation.html', context)


def pets(request):
    context = dict(current_user=request.user)
    context["pet_objects"] = Pet.objects.all().order_by("name")

    return render(request, 'pets.html', context)


class PetFormUpdate(ModelForm):
    class Meta:
        model = Pet
        fields = '__all__'
        labels = {'name': 'Name of Pet'}
        widgets = {'born': DateInput(format=["%Y-%m-%d"], )}

        help_texts = {
            'breed': 'If you don\'t know, just guess',
            'owner': 'Do you Own this dog?',
            'description': 'Something short, sweet, and fun',
        }


class PetUpdateView(UpdateView):
    template_name = "pet_update.html"
    model = Pet
    form_class = PetFormUpdate
    help_texts = None

    def form_valid(self, form):
        send_mail(subject="Puppy Pic API",
                  message="Someone updated a pet",
                  from_email=settings.EMAIL_HOST_USER,
                  recipient_list=[settings.ADMIN_EMAIL],
                  fail_silently=False)
        return super(PetUpdateView, self).form_valid(form)


def send_email(name, user_data):
    # subject = form_data.cleaned_data['subject']
    subject = 'Puppy Pic API'

    try:
        email = user_data.email
    except:
        email = 'INVALID EMAIL'

    message = f'''Puppy Pic Alert!
        {user_data} added a new photo called {name}
    '''

    send_mail(subject,
              message,
              from_email=settings.EMAIL_HOST_USER,
              recipient_list=[settings.ADMIN_EMAIL, email],
              fail_silently=False)
