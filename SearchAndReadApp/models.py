from typing import Any
from django.db import models
from django.db.models import F

# Create your models here.
class Story(models.Model):
    title_and_user = models.CharField(max_length=200, primary_key=True)
    story = models.TextField()
    read = models.BooleanField(default=False)
    pub_date = models.DateField("date published")
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)

    class Meta:
        ordering = [(F("likes") - F("dislikes"))*(-1)]

class Opinion(models.Model):
    st = models.ForeignKey(Story, on_delete=models.CASCADE)
    liked = models.IntegerField(default=0)
    username = models.CharField(max_length=200)