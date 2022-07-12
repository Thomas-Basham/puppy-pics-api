from rest_framework import serializers
from .models import PuppyPic, Pet


class SnackSerializer(serializers.ModelSerializer):
    class Meta:
        fields = "__all__"
        model = PuppyPic


class PetSerializer(serializers.ModelSerializer):
    class Meta:
        fields = "__all__"
        model = Pet
