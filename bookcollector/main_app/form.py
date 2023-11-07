from django.forms import ModelForm
from .models import Review

class ReviewForm(ModelForm):
  class Meta: #addional functionalty to access and use CBV
    model = Review
    fields = ['date', 'rate', 'review']