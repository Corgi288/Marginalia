from django.urls import path, include
from . import views
from django.conf.urls.static import static
from django.conf import settings

app_name = 'books'

urlpatterns = [
    path('', views.book_list_view, name='book_feed'),
    path('details/<str:book_slug>/', views.books_details, name='details'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)