from django.shortcuts import render,redirect
from todo.models import TODOO
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.models import User
from django.db import models


def signup(request) :
    if request.method=='POST' :
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['pwd']
        user=User.objects.create_user(username,email,password)
        user.save()
        return redirect('/loginn')
    return render(request,'signup.html',{})

def loginn(request) :
    if request.method=='POST' :
        username=request.POST['fmw']
        password=request.POST['pwd']
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('/todopage')
        else :
            return redirect('/loginn')
    return render(request,'loginn.html',{})

def todopage(request) :
    if request.method=='POST' :
        title=request.POST['title']    
        obj=TODOO(title=title,user=request.user)
        obj.save()
        user=request.user
        res=TODOO.objects.filter(user=user).order_by('-date')
        return redirect('/todopage',{'res':res})
    user=request.user
    res=TODOO.objects.filter(user=user).order_by('-date')
    return render(request,'todo.html',{'res':res})

def logoutt(request):
    logout(request)
    return redirect('/loginn')

def edit_todo(request,srno):
      if request.method=='POST' :
        title=request.POST['title']    
        obj=TODOO.objects.get(srno=srno)
        obj.title=title
        obj.save()
        user=request.user
        return redirect('/todopage')

        
      obj=TODOO.objects.get(srno=srno)
      return render(request,'edit_todo.html',{'obj':obj})

def delete_todo(request,srno):
    obj=TODOO.objects.get(srno=srno)
    obj.delete()
    return redirect('/todopage')
