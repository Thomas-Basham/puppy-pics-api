from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone
from django.urls import reverse
from cloudinary.models import CloudinaryField
from django.dispatch import receiver
from django.db.models.signals import pre_delete
import cloudinary.uploader

from django.utils.datetime_safe import strftime, date


# Create your models here.


class Pet(models.Model):
    name = models.CharField(max_length=20)
    breed = models.CharField(max_length=64, blank=True)
    owner = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, blank=True)
    born = models.DateField(blank=True)

    def __str__(self):
        return self.name

    def age(self):
        import datetime
        return int((datetime.date.today() - self.born).days / 365.25)

    def get_profile_pic(self):
        return PuppyPic.objects.filter(pet=self.id)


    def save(self, *args, **kwargs):
        self.name = self.name.capitalize()
        return super().save(*args, **kwargs)


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
        return reverse("puppy_pics_list")  # , args=[str(self.id)]


@receiver(pre_delete, sender=PuppyPic)
def photo_delete(sender, instance, **kwargs):
    cloudinary.uploader.destroy(instance.img.public_id)
