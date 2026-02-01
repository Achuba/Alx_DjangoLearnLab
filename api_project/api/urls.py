# api/urls.py
from django.urls import path
from . import views  # or specific views

urlpatterns = [
    path('books/', views.BookList.as_view(), name='book-list'),
]

