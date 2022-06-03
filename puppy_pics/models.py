from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse


# Create your models here.
class PuppyPic(models.Model):
    name = models.CharField(max_length=64)
    description = models.CharField(max_length=64, default='')
    img = models.ImageField(blank=True, null=True, upload_to='media/')
    added_by = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("puppy_pic_detail", args=[str(self.id)])
