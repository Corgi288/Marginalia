from django.shortcuts import render, get_object_or_404
import requests
from .models import Books


def book_list_view(request):
    return render(request, 'books/index.html', {'books': Books.objects.all()})

def books_details(request, book_slug):
    book = get_object_or_404(Books, slug=book_slug)

    return render(request, 'books/booksDetails.html',{
        'book': book
    })