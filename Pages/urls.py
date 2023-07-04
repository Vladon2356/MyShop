from django.urls import path
from django.views.generic import TemplateView

from Pages import views

urlpatterns = [
    path('main/', views.Home.as_view(), name='Home'),
    path('on_order/', views.ToOrderView.as_view(), name='on_order'),
    path('about_us/', TemplateView('Pages/about_us.html'), name='about_us'),
    path('contacts/', TemplateView('Pages/constructor.html'), name='contacts'),
    path('other/', TemplateView('Pages/other.html'), name='other'),
    path('to_order/', TemplateView('Pages/constructor.html'), name='to_order'),
]
