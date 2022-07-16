from django.contrib import admin
from .models import PuppyPic, Pet
from .forms import CustomAdminAuthenticationForm
# Register your models here.
admin.site.register(PuppyPic)
admin.site.register(Pet)

admin.site.login_form = CustomAdminAuthenticationForm

