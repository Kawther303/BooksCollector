from django.db import models
from django.urls import reverse
from datetime import date
#auth ---------
from django.contrib.auth.models import User
# Create your models here.

class Reward(models.Model):
  name = models.CharField(max_length=50)
  provider = models.CharField(max_length=50)

  def __str__(self):
    return self.name
  
  def get_absolute_url(self):
    return reverse('rewards_detail', kwargs={'pk': self.id})

# Create your models here.

RATES =(
  ('0','No Rate'),
  ('1','Low'),
  ('2','Good'),
  ('3','Great')
)
class Book(models.Model):
  name = models.CharField(max_length=100)
  author = models.CharField(max_length=100)
  description = models.TextField(max_length=200)
  release_year = models.IntegerField()
  image = models.ImageField(upload_to = "main_app/static/uploads", default= "" )
  rewards = models.ManyToManyField(Reward)
  #auth ---------
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  #-----------------------------
  def get_absolute_url(self):
    return reverse('detail', kwargs={'book_id': self.id})
  def __str__(self):
    return f" {self.name}"

  def well_review(self):
    return self.review_set.filter(rate='3').count()

class Review(models.Model):
  date = models.DateField('review date')
  rate = models.CharField(max_length=1 , choices=RATES, default =RATES[0][0])
  review = models.CharField(max_length=100)
  book = models.ForeignKey(Book, on_delete=models.CASCADE)
  
  def __str__(self):
    return f"{self.book.name} {self.get_rate_display()} on {self.date}"
  
  class Meta:
    ordering = ['-date'] 