from django.contrib import admin
from .models import Product
# Register your models here.


class productAdmin(admin.ModelAdmin):
    model = Product
    list_display = ['name', 'price']

admin.site.register(Product, productAdmin)