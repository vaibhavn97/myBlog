from django import forms 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile

class UserRegisterationForm(UserCreationForm):
    username = forms.CharField(widget=forms.widgets.TextInput(attrs={'class':'form-control'}))
    password1 = forms.CharField(widget=forms.widgets.PasswordInput(attrs={'class':'form-control'}))
    password2 = forms.CharField(widget=forms.widgets.PasswordInput(attrs={'class':'form-control'}))
    email = forms.EmailField(widget=forms.widgets.EmailInput(attrs={'class':'form-control'}))
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'email']

class UserUpdationForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['profile_pic','first_name', 'last_name', 'bio']