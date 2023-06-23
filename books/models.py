from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=160)
    author = models.CharField(max_length=150)
    published_date = models.DateField()

    def __str__(self):
        return self.title
