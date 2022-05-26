from django.db import models
from django.contrib.auth import get_user_model


# Create your models here.
class PuppyPic(models.Model):
    name = models.CharField(max_length=64)
    description = models.CharField(max_length=64, default='')
    img_url = models.URLField(max_length=200)
    added_by = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    def __str__(self):
        return self.name
