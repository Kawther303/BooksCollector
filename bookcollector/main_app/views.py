from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Book, Reward
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from .form import ReviewForm
from django.views.generic import ListView, DetailView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
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

class BookCreate(LoginRequiredMixin,CreateView):
  model = Book
  # fields ='__all__'
  fields = ['name','image','release_year','author','description']
  def form_valid(self, form):
    form.instance.user = self.request.user
    return super().form_valid(form)

class BookUpdate(LoginRequiredMixin,UpdateView):
  model = Book
  fields=['description','release_year']

class BookDelete(LoginRequiredMixin,DeleteView):
  model=Book
  success_url = '/books/'

def home(request):  
  return render(request, 'index.html')

def about(request):
  return render(request, 'about.html')
@login_required
def books_index(request):
  # Select * from main_app_book
  books = Book.objects.filter(user=request.user)
  # books = Book.objects.all()
  return render(request, 'books/index.html', {'books': books})

@login_required
def books_detail(request, book_id):
  # select * from main_app_book where id = book_id
  book = Book.objects.get(id=book_id)
  review_form = ReviewForm()
  reward_book_doesnot_have= Reward.objects.exclude(id__in= book.rewards.all().values_list('id'))
  return render(request, 'books/detail.html', {"book" : book, 'review_form':review_form, 'rewards':reward_book_doesnot_have})

@login_required
def add_review(request, book_id):
  form = ReviewForm(request.POST)
  if form.is_valid():
    new_review = form.save(commit = False)
    new_review.book_id = book_id
    new_review.save()
  return redirect('detail', book_id = book_id) 


class RewardList(LoginRequiredMixin,ListView):
  model = Reward

class RewardDetail(LoginRequiredMixin,DetailView):
  model = Reward

class RewardCreate(LoginRequiredMixin,CreateView):
  model = Reward
  fields = ['name','provider']

class RewardUpdate(LoginRequiredMixin,UpdateView):
  model = Reward
  fields = ['name','provider']

class RewardDelete(LoginRequiredMixin,DeleteView):
  model = Reward
  success_url = '/rewards/'

@login_required
def assoc_reward(request, book_id,reward_id):
  Book.objects.get(id=book_id).rewards.add(reward_id)
  return redirect('detail', book_id=book_id)

@login_required
def unassoc_reward(request, book_id,reward_id):
  Book.objects.get(id=book_id).rewards.remove(reward_id)
  return redirect('detail', book_id=book_id)

def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('index')
    else:
      error_message= 'Invalid Signup - Please try again!',form.error_messages
  
  form = UserCreationForm()
  context = {'form': form,'error_message': error_message}
  return render(request,'registration/signup.html',context)