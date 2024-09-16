from django import forms
from .models import Order

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['customer_name', 'customer_email', 'amount']
        widgets = {
            'amount': forms.NumberInput(attrs={'step': '0.01'}),
        } 