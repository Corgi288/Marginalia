from django.contrib.auth import get_user_model
from django.views.generic import DetailView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse

User = get_user_model()

class ProfileDetailView(DetailView):
    model = User
    template_name = 'user/profile_detail.html'
    context_object_name = 'profile' 
    
    slug_url_kwarg = 'user_uuid'  
    slug_field = 'uuid'           

class ProfileUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = User
    fields = ['description', 'avatar'] 
    template_name = 'user/profile_edit.html'
    
    slug_url_kwarg = 'user_uuid' 
    slug_field = 'uuid' 

    def test_func(self):
        user_to_edit = self.get_object()
        return self.request.user == user_to_edit
        
    def get_success_url(self):
        return reverse('user:profile_detail', kwargs={'user_uuid': self.request.user.uuid})