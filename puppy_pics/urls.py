from django.urls import path
from .views import PuppyPicList, PuppyPicDetail

urlpatterns = [
    path("", PuppyPicList.as_view(), name="puppy_pic_list"),
    path("<int:pk>/", PuppyPicDetail.as_view(), name="puppy_pic_detail")
]
