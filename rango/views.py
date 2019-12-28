from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse('Rango says hey there partner!')

def about(request):
    return HttpResponse("Rango says here is the about page!<br/> <a href='/rango/about/about1'>About</a>")

def about1(request):
    return HttpResponse('Finally you came there,Hero..')

# Create your views here.
