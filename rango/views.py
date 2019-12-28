from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    context_dict = {'boldmessage':'Crunchy,creamy,cookie,candy,cupcake!'}    
    return render(request,'rango/index.html',context=context_dict)


def about(request):
    return HttpResponse("Rango says here is the about page!<br/> <a href='/rango/about/about1'>About</a>")

def about1(request):
    return HttpResponse('Finally you came there,Hero..')

# Create your views here.
