from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone
from django.urls import reverse
from cloudinary.models import CloudinaryField


# Create your models here.
class Pet(models.Model):
    name = models.CharField(max_length=20)
    born = models.DateField()

    def __str__(self):
        return self.name


class PuppyPic(models.Model):
    img = CloudinaryField('img')
    name = models.CharField(max_length=64)
    description = models.CharField(max_length=64, default='')
    added_by = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    date_added = models.DateTimeField(default=timezone.now())
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE, related_name="images", default=1)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("puppy_pics_list") #, args=[str(self.id)]

