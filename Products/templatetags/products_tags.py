from django import template

from Products.models import Category, Products, ImagesForSlider

register = template.Library()


@register.simple_tag()
def get_categories():
    return Category.objects.all()


@register.simple_tag()
def get_products_by_category(pk):
    return Products.objects.filter(category_id=pk)


@register.simple_tag()
def get_images_for_slider():
    return ImagesForSlider.objects.filter(in_slider=True)
