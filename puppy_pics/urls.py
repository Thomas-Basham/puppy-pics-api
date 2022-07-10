from django.urls import path
from .views import PuppyPicList, PuppyPicDetail, PetList, PetDetail

urlpatterns = [
    path("", PuppyPicList.as_view(), name="puppy_pic_list"),
    path("<int:pk>/", PuppyPicDetail.as_view(), name="puppy_pic_detail"),
    path("pets/", PuppyPicList.as_view(), name="puppy_pic_list"),
    path("pets/<int:pk>/", PuppyPicDetail.as_view(), name="puppy_pic_detail")
]
