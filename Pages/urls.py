from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import *

urlpatterns = [
    path('main/', Home.as_view(), name='Home'),
    path('about_us/', about_us, name='about_us'),
    path('other/', other, name='other'),
    path('contacts/', contacts, name='contacts'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
