from rest_framework import serializers
from .models import PuppyPic


class SnackSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ("id", "name", "img_url", "description", "added_by")
        model = PuppyPic
