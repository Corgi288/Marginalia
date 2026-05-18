from django.contrib import admin
from .models import Book, Discussion

class BooksAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'genre', 'year', 'is_published') 
    list_filter = ('genre', 'author') 
    search_fields = ('title', 'author')
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Book, BooksAdmin)

class DiscussionAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'book', 'created_at')
    list_filter = ('created_at', 'author', 'book')
    search_fields = ('title', 'description')
    readonly_fields = ('created_at',)
    
admin.site.register(Discussion, DiscussionAdmin)
# Register your models here.
