from django.db import models

# Create your models here.


class Book(models.Model):
    book = models.CharField(max_length=30)
    title = models.CharField(max_length=30)