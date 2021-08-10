from django.contrib import admin

from .models import Products, Category


class ProductsAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'photos', 'price', 'created', 'is_published']
    list_display_links = ['title', 'category', 'photos', 'price']
    search_fields = ['title', 'price', 'category']
    prepopulated_fields = {'slug': ('title',)}


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title']
    list_display_links = ['title']
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Products, ProductsAdmin)
admin.site.register(Category, CategoryAdmin)
