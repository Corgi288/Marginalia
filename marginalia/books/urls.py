from django.urls import path, include
from django.contrib.auth.views import LogoutView
from .views import  Book_List, Book_Detail, RegisterView, Login
from django.conf.urls.static import static
from django.conf import settings
from . import views

app_name = 'books'

urlpatterns = [
    path('', Book_List.as_view(), name='book_feed'),
    path('details/<str:book_slug>/', Book_Detail.as_view(), name='details'),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', Login.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)