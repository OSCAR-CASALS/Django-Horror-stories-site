from django.urls import path
from . import views

urlpatterns = [
    path('', views.IntroduceDataForm, name="RegistrationPage"),
]