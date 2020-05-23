from django.urls import reverse
from django.db import models

# Create your models here.


class Article(models.Model):
    article = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('home')
