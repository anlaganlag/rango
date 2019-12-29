from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    context_dict = {'boldmessage':'Crunchy,creamy,cookie,candy,cupcake!'}    
    return render(request,'rango/index.html',context=context_dict)


def about(request):
    
    context_dict = {'slogon':'Be the best about page!',
                    'gal':'Galfond'}    
    return render(request,'rango/about.html',context=context_dict)


def about1(request):
    return HttpResponse('Finally you came there,Hero..I say no more about....')


