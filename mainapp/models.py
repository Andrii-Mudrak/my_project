from django.db import models
from django.core.validators import MinLengthValidator, int_list_validator
from datetime import datetime
from django.contrib.auth.models import User


# Create your models here.

class Comment(models.Model):
    id = models.BigAutoField(primary_key=True)
    content = models.TextField('content', max_length=400, blank=False)
    created_at = models.DateTimeField('created_at', default=datetime.utcnow)
    deleted_at = models.DateTimeField('deleted_at', null=True)
    user_id = models.ForeignKey('Profile', on_delete=models.SET_NULL, null=True)
    product_id = models.ForeignKey('Product', on_delete=models.SET_NULL, null=True)

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
    name = models.CharField('name', max_length=100, blank=False)
    first_name = models.CharField('First name', max_length=32, default='First name')
    last_name = models.CharField('Last name', max_length=32, default='Last name')
    email = models.CharField('email', max_length=40, default='1@get.com')
    phone = models.CharField('phone', max_length=12, blank=False,
                             validators=[int_list_validator(sep=''),
                                         MinLengthValidator(7)],
                             default='380671234567')
    created_at = models.DateTimeField('created_at', default=datetime.utcnow)
    updated_at = models.DateTimeField('updated_at', default=datetime.utcnow)
    # deleted_at = models.DateTimeField('deleted_at', null=True, default=deleted_time)
    is_verified = models.BooleanField('verified', default=True)
    user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name
