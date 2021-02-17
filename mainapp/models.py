from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.


class Comment(models.Model):
    id = models.BigAutoField(primary_key=True)
    content = models.TextField('content', max_length=400, blank=False)
    created_at = models.DateTimeField('created_at', default=datetime.utcnow)
    deleted_at = models.DateTimeField('deleted_at', null=True)
    user_id = models.ForeignKey('Profile', on_delete=models.CASCADE, null=True)
    product_id = models.ForeignKey('Product', on_delete=models.SET_NULL, null=True)
    revised = models.BooleanField('revised', default=False)

    @property
    def __str__(self):
        return self.content


class Product(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.CharField('title', max_length=100, blank=False)
    content = models.TextField('content', max_length=400, blank=False)
    created_at = models.DateTimeField('created_at', default=datetime.utcnow)
    deleted_at = models.DateTimeField('deleted_at', null=True)
    is_active = models.BooleanField('is_active', default=True)
    author = models.ForeignKey('Profile', on_delete=models.SET_NULL, null=True)
    image = models.ImageField(null=True, blank=True, upload_to="images/",
                              default='images/oops.jpeg')

    def __str__(self):
        return self.content


class Responce(models.Model):
    id = models.BigAutoField(primary_key=True)
    message = models.CharField('message', max_length=100, blank=False)
    created_at = models.DateTimeField('created_at', default=datetime.utcnow)
    deleted_at = models.DateTimeField('deleted_at', null=True)
    product = models.ForeignKey('Product', on_delete=models.SET_NULL, null=True)
    author = models.ForeignKey('Profile', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.message


class Profile(models.Model):
    id = models.BigAutoField(primary_key=True)
    # name = models.CharField('name', max_length=100, blank=False)
    first_name = models.CharField('First name', max_length=32, default='First name')
    last_name = models.CharField('Last name', max_length=32, default='Last name')
    email = models.CharField('email', max_length=40, default='1@get.com')
    phone = PhoneNumberField(blank=True)
    created_at = models.DateTimeField('created_at', default=datetime.utcnow)
    updated_at = models.DateTimeField('updated_at', default=datetime.utcnow)
    user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        name = self.first_name + " " + self.last_name
        return name
