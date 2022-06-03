from django.views.generic import CreateView
from rest_framework import generics
from .serializers import SnackSerializer
from .models import PuppyPic


class PuppyPicList(generics.ListCreateAPIView, CreateView):
    queryset = PuppyPic.objects.all()
    serializer_class = SnackSerializer
    model = PuppyPic
    template_name = 'puppy_pic_list.html'
    fields = ["name", "img", "description", "added_by"]


class PuppyPicDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = PuppyPic.objects.all()
    serializer_class = SnackSerializer

