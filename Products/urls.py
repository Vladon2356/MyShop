from django.urls import path
from .views import *
urlpatterns = [
     path('<str:slug>/', ShowProduct.as_view(), name='show_by_name'),
     path('category/<str:slug>/', ShowByCategory.as_view(), name='show_by_categories'),
]