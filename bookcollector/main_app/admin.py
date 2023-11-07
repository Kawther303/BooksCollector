from django.contrib import admin

# Register your models here.
from .models import Book
from .models import Review
from .models import Reward

admin.site.register(Book)
admin.site.register(Review)
admin.site.register(Reward)