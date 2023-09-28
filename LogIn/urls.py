from django.urls import path
from . import views

urlpatterns =[
    path('', views.LogIn, name='LogInPage'),
    path('PublishStory/', views.PublishStory, name='PublishStory'),
    path('Published/', views.publishedStory, name='Published')
]