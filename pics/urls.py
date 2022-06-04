from django.urls import path

from .views import puppy_pic_view

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', puppy_pic_view, name='upload'),
    # path('upload/', upload, name='upload'),
    # path('<int:pk>', SnackDetailView.as_view(), name='snack_detail'),  # Integer, Primary Key
    # path('create/', PuppyPicCreateView.as_view(), name='puppy_pic_create'),

]
