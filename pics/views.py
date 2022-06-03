
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView
from  puppy_pics.models import PuppyPic
# Create your views here.


class PuppyPicView(ListView):
    template_name = 'puppy_pic_list.html'
    model = PuppyPic


class PuppyPicCreateView(CreateView):
    template_name = 'puppy_pics_create.html'
    model = PuppyPic
    fields = ["name", "img", "description", "added_by"]
