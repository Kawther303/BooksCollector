from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name = 'home'),
    path('about/', views.about, name = 'about'),
    path('books/', views.books_index , name= 'index'),
    path('books/<int:book_id>', views.books_detail , name='detail'),
    path('BookCreate',views.BookCreate.as_view(),name='books_create'),
    path('books/<int:pk>/update/',views.BookUpdate.as_view(),name='books_update'),
    path('Book/<int:pk>/delete/',views.BookDelete.as_view(),name='books_delete'),
    path('book/<int:book_id>/add_review/',views.add_review, name='add_review') ,
  
    path('rewards/',views.RewardList.as_view(), name = 'rewards_index'),
    path('rewards/<int:pk>/',views.RewardDetail.as_view(), name='rewards_detail'), #details/show
    path('rewards/create/',views.RewardCreate.as_view(), name='rewards_create'),#crete
    path('rewards/<int:pk>/update/',views.RewardUpdate.as_view(), name = 'rewards_update'),
    path('rewards/<int:pk>/delete/',views.RewardDelete.as_view(), name = 'rewards_delete'),
# associate a reward with a book
    path('book/<int:book_id>/assoc_book/<int:reward_id>/', views.assoc_reward, name="assoc_reward"),
    path('book/<int:book_id>/unassoc_reward/<int:reward_id>/', views.unassoc_reward, name="unassoc_reward"),
    path('accounts/signup/', views.signup, name ='signup')
]
