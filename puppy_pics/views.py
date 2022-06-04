from django.views.generic import CreateView
from rest_framework import generics
from .serializers import SnackSerializer
from .models import PuppyPic


class PuppyPicList(generics.ListCreateAPIView):
    queryset = PuppyPic.objects.all()
    serializer_class = SnackSerializer
    model = PuppyPic


class PuppyPicDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = PuppyPic.objects.all()
    serializer_class = SnackSerializer

