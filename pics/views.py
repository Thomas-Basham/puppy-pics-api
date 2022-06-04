from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView
from puppy_pics.models import PuppyPic
from puppy_pics.serializers import SnackSerializer
from django.forms import ModelForm
# Create your views here.


class PuppyPicView(ListView):
    template_name = 'puppy_pic_list.html'
    model = PuppyPic


class PhotoForm(ModelForm):
    class Meta:
        model = PuppyPic
        fields = '__all__'


def upload(request):
    context = dict(backend_form=PhotoForm())

    if request.method == 'POST':
        form = PhotoForm(request.POST, request.FILES)
        context['posted'] = form.instance
        if form.is_valid():
            form.save()
        return redirect('puppy_pics_list')

    return render(request, 'upload.html', context)