from django.contrib import admin
from .models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'description', 'price', 'created_at']
    list_editable = ['price']
    ordering = ['created_at']
    search_fields = ['name', 'description']
    list_filter = ['name', 'created_at']
