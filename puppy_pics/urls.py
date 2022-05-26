from django.urls import path
from .views import PuppyPicList, PuppyPicDetail

urlpatterns = [
    path("", PuppyPicList.as_view(), name="snack_list"),
    path("<int:pk>/", PuppyPicDetail.as_view(), name="snack_detail"),
]
