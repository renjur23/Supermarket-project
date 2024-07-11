from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from .models import Category, Products

# Create your views here.
# def register(request):
#     return render(request,'form.html')
def home(request):
    return render(request,'home.html')
def category(request):
        cat_dict={
        'categories':Category.objects.all()
    }
        return render(request,'category.html',cat_dict)
   
def products(request,category_slug=None):
    categories=Category.objects.all()
    products=Products.objects.all()
    
    if category_slug:
        category=get_object_or_404(Category,slug=category_slug)
        products=products.filter(category=category)
    else:
        category=None
        
    context={
        'category':category,
        'categories':categories,
        'products':products,
    }
    
    return render(request,'products.html',context)

    
    #  pro_dict={
    #     'pro':Products.objects.all()
    # }
    #  return render(request,'products.html',pro_dict)
    