from django.db import models

# Create your models here.

class LibraryBooks(models.Model):
    title: models.CharField(max_length=200)
    author: models.CharField(max_length=100)
    published_date: models.DateField
    isbn: models.CharField(max_length=13)

    def __init__(self):
        return self.title

