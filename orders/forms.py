from django.forms import ModelForm
from .models import Order
from django.contrib.auth.models import User
from django import forms

class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = ['user','user_name','pay_price','original_price']