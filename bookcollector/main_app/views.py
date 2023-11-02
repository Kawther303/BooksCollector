from django.shortcuts import render
from django.http import HttpResponse
from .models import Book
# # Create your views here.

# class Book:
#   def __init__(self, name,author, description, release_year):
#     self.name= name
#     self.author = author
#     self.description = description
#     self.release_year= release_year

# books = [
#   Book('xxxx','ccc','Histical Novel',2022),
#   Book('111we','vvv','Story',2020)
# ]

def home(request):  
  return render(request, 'index.html')

def about(request):
  return render(request, 'about.html')

def books_index(request):
  # Select * from main_app_book
  books = Book.objects.all()
  return render(request, 'books/index.html', {'books': books})


def books_detail(request, book_id):
  # select * from main_app_book where id = book_id
  book = Book.objects.get(id=book_id)
  return render(request, 'books/detail.html', {"book" : book})
