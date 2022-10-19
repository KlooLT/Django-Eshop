from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Product


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'email']


def __init__(self, *args, **kwargs):
    super(CustomUserCreationForm, self).__init__(self, *args, **kwargs)
    self.fields['username'].widget.attrs.update({'class': 'form-control'})
    self.fields['password1'].widget.attrs.update({'class': 'form-control'})
    self.fields['password2'].widget.attrs.update({'class': 'form-control'})
    self.fields['email'].widget.attrs.update({'class': 'form-control'})


class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
