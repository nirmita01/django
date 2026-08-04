from django import forms
from .models import User

class UserSignupForm(forms.ModelForm):
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Password'}), label="Confirm Password")

    class Meta:
        model = User 
        fields = ['name', 'email', 'password', 'phone', 'address', 'confirm_password', 'role']