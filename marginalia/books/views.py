from django.views.generic import CreateView, DetailView, ListView
from django.contrib.auth.views import LoginView
from django.views.generic.edit import FormMixin
from django.urls import reverse_lazy
from django.shortcuts import redirect
from .models import Book
from .forms import UserRegistrationForm, DiscussionForm


class Book_List(ListView):
    model = Book
    template_name = 'books/index.html'
    context_object_name = 'page'
    paginate_by = 15

class Book_Detail(FormMixin, DetailView):
    model = Book
    template_name = 'books/booksDetails.html'
    context_object_name = 'book'
    slug_url_kwarg = 'book_slug' 
    
    form_class = DiscussionForm 

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['discussions'] = self.object.discussions.order_by('-created_at')
        
        return context

    def post(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('login')
        
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        topic = form.save(commit=False)
        topic.book = self.object
        topic.author = self.request.user
        topic.save()
        
        return super().form_valid(form)

    def get_success_url(self):
        return self.request.path


class RegisterView(CreateView):
    form_class = UserRegistrationForm
    template_name = 'user/register.html'
    
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        user = form.save(commit=False)
        user.set_password(form.cleaned_data['password'])
        user.save()

        return super().form_valid(form)
    
class Login(LoginView):
    template_name = 'user/login.html'