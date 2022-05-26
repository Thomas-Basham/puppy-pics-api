from rest_framework import generics
from .serializers import SnackSerializer
from .models import PuppyPic


class PuppyPicList(generics.ListCreateAPIView):
    queryset = PuppyPic.objects.all()
    serializer_class = SnackSerializer


class PuppyPicDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = PuppyPic.objects.all()
    serializer_class = SnackSerializer
