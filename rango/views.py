from django.shortcuts import render
from django.http import HttpResponse
from .models import Category

def index(request):

    category_list = Category.objects.order_by('-likes')[:5]
    context_dict = {'categories':category_list}    

    return render(request,'rango/index.html',context=context_dict)


def about(request):
    
    context_dict = {'slogon':'Be the best about page!',
                    'gal':'Galfond'}    
    return render(request,'rango/about.html',context=context_dict)


def about1(request):
    return HttpResponse('Finally you came there,Hero..I say no more about....')



