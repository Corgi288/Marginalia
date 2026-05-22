import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)
    login = models.CharField(max_length=150, unique=True)
    description = models.TextField(blank=True)

    favorite_books = models.ManyToManyField('books.Book', blank=True, related_name='favorited_by_users')
    reading_now_books = models.ManyToManyField('books.Book', blank=True, related_name='reading_now_books')
    planned_books = models.ManyToManyField('books.Book', blank=True, related_name='planned_books')

    USERNAME_FIELD = 'login'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.login
