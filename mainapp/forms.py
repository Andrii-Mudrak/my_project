from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Product, Profile, Comment


class SignUpForm(UserCreationForm):
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'special', 'placeholder': 'Пароль'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'special', 'placeholder': 'Підтвердити пароль'}))

    class Meta(UserCreationForm.Meta):
        model = User
        # I've tried both of these 'fields' declaration, result is the same
        fields = ['username', 'password1', 'password2']


class ProductForm(forms.ModelForm):
    title = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'special', 'placeholder': 'Заголовок'}), max_length=100)
    content = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'special', 'placeholder': 'Опис'}), max_length=400)

    class Meta:
        model = Product
    #     # I've tried both of these 'fields' declaration, result is the same
        fields = ['title', 'content']


class ProfileForm(forms.ModelForm):
    # name = forms.CharField(widget=forms.TextInput(attrs={
    #     'class': 'special', 'placeholder': 'name'}), max_length=100)
    first_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'special', 'placeholder': 'Ім`я'}), max_length=32)
    last_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'special', 'placeholder': 'Прізвище'}), max_length=32)
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'class': 'special', 'placeholder': 'Електронна пошта'}), max_length=64)
    phone = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'special', 'placeholder': '+380671234567'}), max_length=14)

    class Meta:
        model = Profile
        fields = ['first_name', 'last_name', 'email', 'phone']


class CommentForm(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'special', 'placeholder': 'Ваш коментар'}), max_length=400)

    class Meta:
        model = Comment
        fields = ['content']
