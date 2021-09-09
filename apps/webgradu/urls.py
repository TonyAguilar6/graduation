from django.urls import path
from .views import *


urlpatterns = [
    path('', index, name='index'),
    path('services/', services, name='services'),
    path('contact/', contacto, name='contacto'),
    path('about/', about, name='about'),
    path('elements/', elements, name='elements'),
    path('blog/', blog, name='blog'),
    path('blog_details/', blog_details, name='blog_details'),
]
