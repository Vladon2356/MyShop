from django.urls import path
from Products import views
urlpatterns = [
     path('<str:slug>/', views.ShowProduct.as_view(), name='show_by_name'),
     path('category/<str:slug>/', views.ShowByCategory.as_view(), name='show_by_categories'),
]
