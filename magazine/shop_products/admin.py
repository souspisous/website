from django.contrib import admin
from .models import Product, Category


@admin.register(Product)
class BookAdmin(admin.ModelAdmin):
    list_display = ("name", 'id', "text", "time", "category")


@admin.register(Category)
class BookCategory(admin.ModelAdmin):
    list_display = ("name", "id", "time")

