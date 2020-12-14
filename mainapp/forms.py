from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Product, Profile
from datetime import datetime, timedelta


class SignUpForm(UserCreationForm):
    # user = forms.CharField(widget=forms.TextInput(attrs={
    #     'class': 'form-control', 'placeholder': 'Username'}))
    first_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control', 'placeholder': 'First Name'}), max_length=32)
    last_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control', 'placeholder': 'Last Name'}), max_length=32)
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'class': 'form-control', 'placeholder': 'Enter a valid email'}), max_length=64)
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control', 'placeholder': 'Password'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control', 'placeholder': 'Password Again'}))

    class Meta(UserCreationForm.Meta):
        model = User
        # I've tried both of these 'fields' declaration, result is the same
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']
        # fields = UserCreationForm.Meta.fields + ('first_name', 'last_name', 'email')


class ProductForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control', 'placeholder': 'Title'}), max_length=100)
    content = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control', 'placeholder': 'Content'}), max_length=400)

    class Meta:
        model = Product
    #     # I've tried both of these 'fields' declaration, result is the same
        fields = ['title', 'content']


class ProfileForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control', 'placeholder': 'name'}), max_length=100)
    phone = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control', 'placeholder': 'phone'}), max_length=12)


    class Meta:
        model = Profile
        fields = ['name', 'phone']
