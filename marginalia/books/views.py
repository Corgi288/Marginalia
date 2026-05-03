from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import Books


def book_list_view(request):
    books = Books.objects.order_by('?')[:120]

    paginator = Paginator(books, 20)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
    'page_obj': page_obj,
    }

    return render(request, 'books/index.html', {'page_obj': page_obj})

def books_details(request, book_slug):
    book = get_object_or_404(Books, slug=book_slug)

    return render(request, 'books/booksDetails.html',{
        'book': book
    })