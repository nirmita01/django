from django import forms
from .models import User

class Userform(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter Name'}), label = 'Name',)
    email =forms.CharField(widget=forms.EmailInput(attrs={'placeholder': 'Enter Email'}), label = 'Email',)
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Enter password'}), label = 'Password',)
    address = forms.CharField(widget=forms.Textarea(attrs={
        'rows': 2,
        'placeholder': 'Enter Address',
        'style': 'resize:none;'
    }), label = 'Address'),
    class Meta:
        model = User 
        fields = '__all__'