from django.contrib import admin

from core.apps.customers.models import Customer


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ("id", "phone", "token", "created_at")
    list_filter = ("created_at", "updated_at")
    search_fields = ("phone",)
