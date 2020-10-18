from django.db import models

# Create your models here.

class Comments(models.Model):
    id = models.AutoField(primary_key=True)
    content = models.TextField(max_length=400)
    created_at = models.DateTimeField()
    deleted_at = models.DateTimeField()
    user_id = models.ForeignKey('User', on_delete=models.CASCADE)
    product_id = models.ForeignKey('Product', on_delete=models.CASCADE)

    def __str__(self):
        return self.content

class Product(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    content = models.TextField(max_length=400)
    created_at = models.DateTimeField()
    deleted_at = models.DateTimeField()
    is_active = models.BooleanField()
    autor_id = models.ForeignKey('User', on_delete=models.CASCADE)

    def __str__(self):
        return self.content

class Responces(models.Model):
    id = models.AutoField(primary_key=True)
    message = models.CharField(max_length=100)
    created_at = models.DateTimeField()
    deleted_at = models.DateTimeField()
    product_id = models.ForeignKey('Product', on_delete=models.CASCADE)
    autor_id = models.ForeignKey('User', on_delete=models.CASCADE)

    def __str__(self):
        return self.message

class User(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    deleted_at = models.DateTimeField()
    is_verified = models.BooleanField()
    'тут потрібно 1 до 1 юзера вклеїть'