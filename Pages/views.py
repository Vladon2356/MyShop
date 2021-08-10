from django.shortcuts import render
from django.views.generic import ListView
from Products.models import Category


class Home(ListView):
    model = Category
    template_name = 'Pages/main_page.html'
    context_object_name = 'cat'

def about_us(request):
    return render(request, 'Pages/about_us.html')


def other(request):
    return render(request, 'Pages/other.html')


def contacts(request):
    return render(request, 'Pages/contacts.html')

