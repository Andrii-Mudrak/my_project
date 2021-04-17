from django.contrib import admin
# Register your models here.
from mainapp.models import Product, Comment, Responce, Profile

admin.site.register(Product)
admin.site.register(Comment)
admin.site.register(Responce)
admin.site.register(Profile)
