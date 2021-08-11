from django.contrib import admin

from .models import Products, Category, Images, ImagesForSlider, Collection


class ProductsAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'photos', 'price', 'created', 'is_published')
    list_display_links = ('title', 'category', 'photos', 'price')
    search_fields = ('title', 'price', 'category')
    prepopulated_fields = {'slug': ('title',)}
    list_editable = ('is_published',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title',)
    list_display_links = ('title',)
    prepopulated_fields = {'slug': ('title',)}


class ImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'image')
    list_display_links = ('id', 'image')
    search_fields = ('id', 'image')


class ImageForSliderAdmin(admin.ModelAdmin):
    list_display = ('id', 'in_slider')
    list_display_links = ('id',)
    search_fields = ('id', 'in_slider')
    list_editable = ('in_slider',)


class CollectionAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'total_price', 'is_published', 'views')
    list_display_links = ('id', 'title', 'total_price', 'views')
    search_fields = ('id', 'title', 'total_price', 'is_published', 'views')
    prepopulated_fields = {'slug': ('title',)}
    list_editable = ('is_published',)


admin.site.register(Products, ProductsAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Images, ImageAdmin)
admin.site.register(ImagesForSlider, ImageForSliderAdmin)
admin.site.register(Collection, CollectionAdmin)
