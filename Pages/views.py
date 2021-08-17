from django.shortcuts import render
from django.views.generic import ListView,CreateView

from Pages.models import ToOrder
from Products.models import Category
from .forms import ToOrderForm


class Home(ListView):
    model = Category
    template_name = 'base.html'
    context_object_name = 'cat'


def about_us(request):
    return render(request, 'Pages/about_us.html')


class ToOrderView(CreateView):
    form_class = ToOrderForm
    template_name = 'Pages/constructor.html'
    success_url = '/main'


def to_order(request):
    return render(request, 'Pages/constructor.html')


def other(request):
    return render(request, 'Pages/other.html')


def contacts(request):
    return render(request, 'Pages/contacts.html')
