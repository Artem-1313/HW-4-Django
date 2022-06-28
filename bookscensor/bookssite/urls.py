from django.urls import path, include
from .views import BookListView, BookDetailView, ReviewUpdate, ReviewDelete, BookAdd

urlpatterns = [
    path('', BookListView.as_view(), name="index"),
    path('book/<int:pk>/', BookDetailView.as_view(), name="book_detail"),
    path('review_update/<int:pk>/', ReviewUpdate.as_view(), name="review_update"),
    path('review_delete/<int:pk>/', ReviewDelete.as_view(), name="review_delete"),
    path('book_add/', BookAdd.as_view(), name="book_add"),

]