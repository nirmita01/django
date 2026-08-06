from django import forms
from .models import Order


class OrderForm(forms.ModelForm):
    customer = forms.ModelChoiceField(queryset=None,label='Customer')

    order_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}),label='Order Date')

    status = forms.ChoiceField(choices=Order.OrderStatus.choices,label='Status')

    order_details = forms.ModelMultipleChoiceField(queryset=None,widget=forms.CheckboxSelectMultiple,label='Order Details')

    class Meta:
        model = Order
        fields = '__all__'

    