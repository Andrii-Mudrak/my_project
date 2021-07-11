from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from mainapp.models import Product, Profile, Comment
from phonenumber_field.modelfields import PhoneNumberField


class SignUpForm(UserCreationForm):
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'special', 'placeholder': 'xxxxxxx', 'autocomplete': 'off', 'data-toggle': 'p'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'special', 'placeholder': 'Підтвердити пароль'}))

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['username', 'password1', 'password2']
        # widgets = {
        #     "username": TextInput(attrs={'placeholder': 'ex:test', 'autocomplete': 'off'}),
        #     "password": PasswordInput(
        #         attrs={'placeholder': '********', 'autocomplete': 'off', 'data-toggle': 'password'}),
        # }


class ProductForm(forms.ModelForm):
    title = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'special', 'placeholder': 'Заголовок'}), max_length=100)
    content = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'special', 'placeholder': 'Опис'}), max_length=400)
    # image = forms.ImageField(widget=forms.FileInput(attrs={'class':'special'}))

    class Meta:
        model = Product
        fields = ['title', 'content', 'image']


class ProfileForm(forms.ModelForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'special', 'placeholder': 'Ім`я'}), max_length=32)
    last_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'special', 'placeholder': 'Прізвище'}), max_length=32)
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'class': 'special', 'placeholder': 'Електронна пошта'}), max_length=64)
    phone = PhoneNumberField(blank=True)

    class Meta:
        model = Profile
        fields = ['first_name', 'last_name', 'email', 'phone']


class CommentForm(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'special', 'placeholder': 'Ваш коментар'}), max_length=400)

    class Meta:
        model = Comment
        fields = ['content']


class ChangeAccountForm(forms.ModelForm):
    # username = forms.CharField(widget=forms.TextInput(attrs={
    #     'class': 'special', 'placeholder': 'Псевдо'}), max_length=16)
    first_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'special', 'placeholder': 'Ім`я'}), max_length=32)
    last_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'special', 'placeholder': 'Прізвище'}), max_length=32)
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'class': 'special', 'placeholder': 'Електронна пошта'}), max_length=64)
    phone = PhoneNumberField(blank=True)

    class Meta:
        model = Profile
        fields = ['first_name', 'last_name', 'email', 'phone']
