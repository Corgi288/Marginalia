from django.contrib import admin
from .models import Books

class BooksAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'genre', 'year', 'is_published') 
    list_filter = ('genre', 'author') 
    search_fields = ('title', 'author')
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Books, BooksAdmin)
# Register your models here.
