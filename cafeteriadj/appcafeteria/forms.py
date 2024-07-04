# myapp/forms.py
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    nombres = forms.CharField(max_length=100)

    class Meta:
        model = User
        fields = ['username', 'nombres', 'email', 'password1', 'password2']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
            profile = Profile(user=user, nombres=self.cleaned_data['nombres'], correo=self.cleaned_data['email'])
            profile.save()
        return user
