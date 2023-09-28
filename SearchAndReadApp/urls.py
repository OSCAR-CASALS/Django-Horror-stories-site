from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('results/', views.SearchRes, name='results'),
    path('Read/', views.ReadStory, name='Read')
    ]