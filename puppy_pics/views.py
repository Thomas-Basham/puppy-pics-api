from django.views.generic import CreateView
from rest_framework import generics
from .serializers import SnackSerializer, PetSerializer
from .models import PuppyPic, Pet


# Pics
class PuppyPicList(generics.ListCreateAPIView):
    queryset = PuppyPic.objects.all()
    serializer_class = SnackSerializer
    model = PuppyPic


class PuppyPicDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = PuppyPic.objects.all()
    serializer_class = SnackSerializer


# Pets
class PetList(generics.ListCreateAPIView):
    queryset = Pet.objects.all()
    serializer_class = PetSerializer
    model = PuppyPic


class PetDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Pet.objects.all()
    serializer_class = PetSerializer

