from django import forms
from .models import Order


class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['first_name', 'last_name', 'city', 'customer', 'shop']
        widgets = {'customer': forms.HiddenInput(), 'shop': forms.HiddenInput()}