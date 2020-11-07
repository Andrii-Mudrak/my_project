from django.db import models
from django.conf import settings
from django.core.validators import MinLengthValidator, int_list_validator
from datetime import datetime


# Create your models here.

class Comment(models.Model):
    id = models.BigAutoField('id', primary_key=True)
    content = models.TextField('content', max_length=400, blank=False)
    created_at = models.DateTimeField('created_at', default=datetime.utcnow)
    deleted_at = models.DateTimeField('deleted_at', null=True)
    user_id = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    product_id = models.ForeignKey('Product', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.content


class Product(models.Model):
    id = models.BigAutoField('id', primary_key=True)
    title = models.CharField('title', max_length=100, blank=False)
    content = models.TextField('content', max_length=400, blank=False)
    created_at = models.DateTimeField('created_at', default=datetime.utcnow)
    deleted_at = models.DateTimeField('deleted_at', null=True)
    is_active = models.BooleanField('is_active', default=False)
    autor = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.content


class Responce(models.Model):
    id = models.BigAutoField('id', primary_key=True)
    message = models.CharField('message', max_length=100, blank=False)
    created_at = models.DateTimeField('created_at', default=datetime.utcnow)
    deleted_at = models.DateTimeField('deleted_at', null=True)
    product = models.OneToOneField(Product, on_delete=models.SET_NULL, null=True)
    autor = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.message


class Profile(models.Model):
    id = models.BigAutoField('id', primary_key=True)
    name = models.CharField('name', max_length=100, blank=False)
    phone = models.CharField('phone', max_length=12, blank=False,
                             validators=[int_list_validator(sep=''),
                                         MinLengthValidator(12), ],
                             default='380671234567')
    created_at = models.DateTimeField('created_at', default=datetime.utcnow)
    updated_at = models.DateTimeField('updated_at', default=datetime.utcnow)
    deleted_at = models.DateTimeField('deleted _at', null=True)
    is_verified = models.BooleanField('verified', default=False)
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name
