from django.urls import path

from .views import AboutPageView, HomePageView, Profile, Termos

app_name = "pages"

urlpatterns = [
    path("about/", AboutPageView.as_view(), name="about"),
    path("", HomePageView.as_view(), name="home"),
    path("profile/", Profile.as_view(),  name='profile-home'),
    path("termos-de-uso/", Termos.as_view(),  name='termos-de-uso'),

]

