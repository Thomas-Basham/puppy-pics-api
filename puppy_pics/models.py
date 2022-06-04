from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse
from cloudinary.models import CloudinaryField


# Create your models here.
class PuppyPic(models.Model):
    name = models.CharField(max_length=64)
    description = models.CharField(max_length=64, default='')
    # img = models.ImageField(upload_to='media/')
    img = CloudinaryField('img')
    added_by = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("puppy_pics_list") #, args=[str(self.id)]

    # @property
    # def s3_url(self):
    #     return self.img.url

