from django.contrib import admin
from .models import User

class UserAdmin(admin.ModelAdmin):
    list_display = ['login']
    search_fields = ['avatar', 'login', 'description', 'favorite_books','reading_now_books', 'planned_books']
admin.site.register(User, UserAdmin)
# Register your models here.
