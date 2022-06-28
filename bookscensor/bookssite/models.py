from django.contrib.auth.models import User
from django.db import models


# Create your models here.


class Book(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    author = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.title} by {self.author}"


class Review(models.Model):
    RATING = [
        ('5', 5),
        ('4', 4),
        ('3', 3),
        ('2', 2),
        ('1', 1),
    ]
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    review = models.TextField()
    review_create = models.DateTimeField(auto_now_add=True)
    review_update = models.DateTimeField(auto_now=True)
    rating = models.CharField(max_length=1, choices=RATING, default='5')

    def __str__(self):
        return f"Review about {self.book} by user: {self.user}"
