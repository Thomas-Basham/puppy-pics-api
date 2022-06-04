from django.urls import path

from .views import PuppyPicView, upload

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', PuppyPicView.as_view(), name='puppy_pics_list'),
    path('upload/', upload, name='upload'),
    # path('<int:pk>', SnackDetailView.as_view(), name='snack_detail'),  # Integer, Primary Key
    # path('create/', PuppyPicCreateView.as_view(), name='puppy_pic_create'),

]
