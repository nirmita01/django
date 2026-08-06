from django import forms
from .models import Customer

class Customerform(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter Name'}), label = 'Name',)
    email =forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'Enter Email'}), label = 'Email',)
    phone =forms.CharField(widget=forms.NumberInput(attrs={'placeholder': 'Enter Phone'}), label = 'Phone Number',)
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Enter password'}), label = 'Password',)

    class Meta:
        model = Customer 
        fields = '__all__'