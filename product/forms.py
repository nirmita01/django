from django import forms
from .models import Category, Product


class CategoryForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter Category Name'}),label='Name')
    description = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Enter Description'}),label='Description',required=False)

    class Meta:
        model = Category
        fields = '__all__'


class ProductForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter Product Name'}),label='Name')
    description = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Enter Description'}),label='Description',required=False)
    price = forms.DecimalField(widget=forms.NumberInput(attrs={'placeholder': 'Enter Price'}),label='Price')

    class Meta:
        model = Product
        fields = '__all__'