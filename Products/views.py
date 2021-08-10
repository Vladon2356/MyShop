from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
from .models import Products



class ShowByCategory(ListView):
    model = Products
    template_name = 'Products/show_by_category.html'
    context_object_name = 'products'
    allow_empty = False

    def get_queryset(self):
        return Products.objects.filter(category__slug=self.kwargs['slug'], is_published=True).select_related('category')


class ShowProduct(DetailView):
    model = Products
    template_name = 'Products/show_product.html'
    context_object_name = 'product'

    def get_queryset(self):
        return Products.objects.filter(slug=self.kwargs['slug'])


def show_product(request, slug):
    pr = Products.objects.filter(slug=slug)
    return render(request, 'Products/show_product.html', {'products': pr})


