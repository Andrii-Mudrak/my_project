from django.db import models
from django.conf import settings
from django.core.validators import MinLengthValidator, int_list_validator
from datetime import datetime

# Create your models here.

class Comments(models.Model):
    id = models.BigAutoField(primary_key=True)
    content = models.TextField(max_length=400, blank=False)
    created_at = models.DateTimeField(default=datetime.now())
    deleted_at = models.DateTimeField(null=True)
    user_id = models.ForeignKey('User', on_delete=models.SET_NULL, null=True)
    product_id = models.ForeignKey('Product', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.content

class Product(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=100, blank=False)
    content = models.TextField(max_length=400, blank=False)
    created_at = models.DateTimeField(default=datetime.now())
    deleted_at = models.DateTimeField(null=True)
    is_active = models.BooleanField(default=False)
    autor_id = models.ForeignKey('User', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.content

class Responces(models.Model):
    id = models.BigAutoField(primary_key=True)
    message = models.CharField(max_length=100, blank=False)
    created_at = models.DateTimeField(default=datetime.now())
    deleted_at = models.DateTimeField(null=True)
    product_id = models.ForeignKey('Product', on_delete=models.SET_NULL, null=True)
    autor_id = models.ForeignKey('User', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.message

class Profile(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=100, blank=False)
    phone = models.CharField(max_length=12, blank=False,
                             validators=[int_list_validator(sep=''),
                                         MinLengthValidator(12),],
                             default='380671234567')
    created_at = models.DateTimeField(default=datetime.now())
    updated_at = models.DateTimeField(default=datetime.now())
    deleted_at = models.DateTimeField(null=True)
    is_verified = models.BooleanField(default=False)
    user_id = models.ForeignKey('User', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name


class User(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,
                                verbose_name = 'Profile',
                                on_delete = models.SET_NULL,
                                null=True
                                )
    #password = models.CharField(max_length = 10, blank=False)

    #username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}))
    first_name = models.CharField(max_length=32, help_text='First name')
    last_name=models.CharField(max_length=32, help_text='Last name')
    email=models.EmailField(max_length=64, help_text='Enter a valid email address')
    password1=models.CharField(max_length=20, help_text='Input a passaword')



    def __str__(self):
        return self.user
