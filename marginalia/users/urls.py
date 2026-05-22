from django.urls import path
from .views import ProfileDetailView, ProfileUpdateView

app_name = 'user'

urlpatterns = [
    path('profile/<uuid:user_uuid>/', ProfileDetailView.as_view(), name='profile_detail'),
    path('profile/<uuid:user_uuid>/edit/', ProfileUpdateView.as_view(), name='profile_edit'),
]