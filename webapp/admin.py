from django.contrib import admin

from .forms import ProductForm
from product.models import Product


class ProductAdmin(admin.ModelAdmin):
    form = ProductForm


admin.site.register(Product, ProductAdmin)
