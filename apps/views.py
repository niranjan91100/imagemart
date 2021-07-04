from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.models import User
from .models import *
from apps.models import *
from django.contrib.auth import authenticate,logout,login
from django.contrib import messages

def home(request):
    image=Image.objects.all()
    cats=Category.objects.all()
    data={'image':image,'cats':cats}
    return render(request,'home.html',data)

def show_category(request,cid):

    cats = Category.objects.all()
    catego=Category.objects.get(pk=cid)
    image=Image.objects.filter(cat=catego)
    data = {'image': image, 'cats': cats}
    return render(request, 'home.html', data)
