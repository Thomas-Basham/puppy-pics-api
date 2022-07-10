from django.shortcuts import render, redirect
from django.views.generic import ListView
from puppy_pics.models import PuppyPic, Pet
from django.forms import ModelForm
from django.forms import modelformset_factory
from django import forms
from django.contrib.auth.models import User
# Create your views here.
from django.contrib import messages


def puppy_pic_view(request):
    ImageFormSet = modelformset_factory(PuppyPic, form=PhotoForm)  # , extra=3

    context = dict(backend_form=PhotoForm())
    context["dataset"] = PuppyPic.objects.all().order_by("-id")
    context["pet_form"] = PetForm()
    context["formset"] = ImageFormSet(queryset=PuppyPic.objects.none())
    if request.method == 'POST':
        pet_form = PetForm(request.POST)
        formset = ImageFormSet(request.POST, request.FILES)
        if pet_form.is_valid() and formset.is_valid():
            if Pet.objects.filter(name=pet_form.cleaned_data['name']):
                for form in formset.cleaned_data:
                    if form:
                        image = form['img']
                        name = form['name']
                        description = form['description']
                        added_by = form['added_by']

                        PuppyPic.objects.create(img=image, pet=Pet.objects.filter(name=pet_form.cleaned_data['name'])[0],
                                                name=name,description=description, added_by=added_by,
                                                )
            else:
                pet_obj = pet_form.save()

                for form in formset.cleaned_data:
                    if form:

                        image = form['img']
                        name = form['name']
                        description = form['description']
                        added_by = form['added_by']

                        PuppyPic.objects.create(img=image, pet=pet_obj, name=name,
                                                description=description, added_by=added_by,
                                                )
        return redirect('upload')

    return render(request, 'upload.html', context)


class PhotoForm(ModelForm):
    class Meta:
        model = PuppyPic
        # fields = '__all__'
        exclude = ('date_added', 'pet')  # , 'added_by'
        labels = {
            'name': 'Title of Photo',
            'img': 'Image'
        }


class DateInput(forms.DateInput):
    input_type = "date"
    def __init__(self, **kwargs):
        kwargs["format"] = "%Y-%m-%d"
        # kwargs["format"] = "%d-%m-%Y"
        super().__init__(**kwargs)


class PetForm(ModelForm):
    class Meta:
        model = Pet
        fields = '__all__'
        labels = {
            'name': 'Name of Pet'
        }
        widgets = {
            'born': DateInput(format=["%Y-%m-%d"],),

        }