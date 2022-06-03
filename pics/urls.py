from django.urls import path

from .views import PuppyPicView, PuppyPicCreateView

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', PuppyPicView.as_view(), name='puppy_pics_list'),
    path('create/', PuppyPicCreateView.as_view(), name='puppy_pic_create'),

]