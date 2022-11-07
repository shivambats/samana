from django.contrib import admin

# Register your models here.
from .models import Product, Variant, Attribute, Category, Brand

admin.site.register(Product)
admin.site.register(Variant)
admin.site.register(Attribute)
admin.site.register(Brand)
admin.site.register(Category)
