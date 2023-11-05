from django.db import models
from django.urls import reverse

# Create your models here.
from django.db import models

# Create your models here.

class Book(models.Model):
  name = models.CharField(max_length=100)
  author = models.CharField(max_length=100)
  description = models.TextField(max_length=200)
  release_year = models.IntegerField()
  image= models.ImageField(upload_to = "main_app/static/uploads", default= "" )
  def get_absolute_url(self):
    return reverse('detail', kwargs={'book_id': self.id})

