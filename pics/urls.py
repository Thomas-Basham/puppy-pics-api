from django.urls import path

from .views import puppy_pic_view, register_request,\
    login_request, logout_request, documentation, pets, PetUpdateView

urlpatterns = [
    path('', puppy_pic_view, name='upload'),
    path("register", register_request, name="register"),
    path("login", login_request, name="login"),
    path("logout", logout_request, name="logout"),
    path("documentation", documentation, name="documentation"),
    path("pets", pets, name="pets"),
    path('<int:pk>/update/', PetUpdateView.as_view(), name='pet_update'),

]
