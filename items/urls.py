from django.contrib import admin
from django.urls import path,include
from .views import *
urlpatterns=[
    path('',home,name='home'),
    #  path('form',register,name='form'),
    path('Products/',products,name='products'),
    path('Products/<slug:category_slug>/',products,name='products_by_category'),
    path('Products/<slug:slug>/',products,name='products_detail'),
    path('Category/',category,name='category')
 
] 