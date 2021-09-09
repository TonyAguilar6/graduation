from django.shortcuts import render
from.models import *
# Create your views here.

def index(request):
    return render(request, 'index.html')
def services(request):
    allpaquete = paquete.objects.all()
    return render(request, 'services.html', {'allpaquete':allpaquete} )

def contacto(request):
    return render(request, 'contact.html')

def about(request):
    return render(request, 'about.html')

def elements(request):
    return render(request, 'elements.html')

def blog(request):
    return render(request, 'blog.html')
def blog_details(request):
    return render(request, 'blog_details.html')
