from django import forms
from django.contrib.auth import get_user_model
from .models import Discussion

User = get_user_model()

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Passwor'}))
    password_confirm = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Enter your password again'}))

    class Meta:
        model = User
        fields = ['login', 'username', 'description'] 
    def clean_clean_password(self):
        pass

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        password_confirm = cleaned_data.get("password_confirm")

        if password != password_confirm:
            raise forms.ValidationError("Wrong password")
        return cleaned_data


class UserLoginForm(forms.Form):
    login = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Your login'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'password'}))


class DiscussionForm(forms.ModelForm):
    title = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Про що хочете поговорити?', 'style': 'width: 100%; padding: 10px;'})
    )
    description = forms.CharField(
        widget=forms.Textarea(attrs={'placeholder': 'Поділіться думками...', 'rows': 5, 'style': 'width: 100%; padding: 10px;'}),
        required=False
    )

    class Meta:
        model = Discussion 
        fields = ['title', 'description',]  