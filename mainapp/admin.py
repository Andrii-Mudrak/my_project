from django.contrib import admin
# Register your models here.
from .models import Product, Comments, Responces, Profile

admin.site.register(Product)
admin.site.register(Comments)
admin.site.register(Responces)
admin.site.register(Profile)