from django.contrib import admin

from .models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'is_visible', 'created_at')
    list_filter = ('is_visible', 'created_at', 'updated_at')
    search_fields = ('title', 'description')
