from django.db.models.base import Model
from django.shortcuts import render, redirect, reverse
from django.views.generic import ListView, DeleteView, UpdateView
from django.http import HttpResponse
from django.views.generic.base import TemplateView
from . import models
from django.shortcuts import get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from datetime import datetime
from .forms import UserRegistrationForm, GeeksForm, GeeksForm2, GeeksForm3, comment,comment2,comment3
# Defining a function which

# will receive request and
# perform task depending
# upon function definition


def hello(request):
    return render(request, 'projectApp/home.html', {'title': 'home'})


@login_required(login_url='/log')
def posts(request):
    all_post = models.Add.objects.all()
    return render(request, 'projectApp/post.html', {'posts': all_post})

@login_required(login_url='/log')
def posts2(request):
    all_post = models.Add2.objects.all()
    return render(request, 'projectApp/post2.html', {'posts': all_post})

@login_required(login_url='/log')
def posts3(request):
    all_post = models.Add3.objects.all()
    return render(request, 'projectApp/post3.html', {'posts': all_post})

def cpost(request):

    if request.method == 'POST':
     form = GeeksForm(request.POST)
     if form.is_valid():
        form.save()
        messages.success(request, 'post have  created successfully')
        return redirect('/posts')

    else:
         form = GeeksForm(request.POST)
    return render(request, 'projectApp/cpost.html', {'form': form})


def cpost2(request):
    if request.method == 'POST':
     form = GeeksForm2(request.POST)
     if form.is_valid():
        form.save()
        messages.success(request, 'post have  created successfully')
        return redirect('/posts2')

    else:
         form = GeeksForm2(request.POST)
    return render(request, 'projectApp/cpost2.html', {'form': form})


def cpost3(request):
    if request.method == 'POST':
        form = GeeksForm3(request.POST)
        if form.is_valid():
         form.save()
         messages.success(request, 'post have  created successfully')
         return redirect('/posts3')

    else:
         form = GeeksForm3(request.POST)
    return render(request, 'projectApp/cpost3.html',{'form': form})

def signin(request):

    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'successfully created')
            return redirect('/hello')
    else:
        form = UserRegistrationForm()
    return render(request, 'projectApp/sign.html', {'form': form})


def log(request):
    if request.method == 'POST':
         username = request.POST['username']
         password = request.POST['password']
         user = authenticate(request, username=username, password=password)
         if user is not None:
             login(request, user)
             return redirect('/hello')
         else:
            return redirect('/log')
    else:
        return render(request, 'projectApp/log.html', {'title': 'Log In'})


def index(request):
    return render(request, 'projectApp/index.html', {'title': 'index'})


def details(request, id):
    obj = get_object_or_404(models.Add, pk=id)
    all_post = models.Add.objects.all()
    return render(request, 'projectApp/details.html', {'posts': all_post, 'obj': obj, })
def detailss(request,id):
    obj = get_object_or_404(models.Add2, pk=id)
    all_post = models.Add2.objects.all()
    return render(request, 'projectApp/details2.html',{'posts': all_post, 'obj': obj, } )

def details3(request,id):
    obj = get_object_or_404(models.Add3, pk=id)
    all_post = models.Add3.objects.all()
    return render(request, 'projectApp/details3.html',{'posts': all_post, 'obj': obj, } )

def addcomment(request,pk):
  eachProduct = models.Add.objects.get(id=pk)
  cot = models.Hello.objects.filter(pk=pk).last()
  form = comment(instance=eachProduct)
  if request.method == 'POST':
     form = comment(request.POST, instance=eachProduct)
     form = comment(request.POST, request.FILES)
     if form.is_valid():
        name = request.user.username
        body = form.cleaned_data['body']
        img =  form.cleaned_data.get('image')
        c =  models.Hello(name=name,image=img ,post= eachProduct, body=body, date_added=datetime.now())
        c.save()
        messages.success(request,'comment successfully')
        return redirect('details',id = pk)
         
        
  else :
         form = comment(request.POST)
  return render(request, 'projectApp/addcomment.html',{'form': form})
def addcomment2(request,pk):
  eachProduct = models.Add2.objects.get(id=pk)
  cot = models.Hello2.objects.filter(pk=pk).last()
  form = comment2(instance=eachProduct)
  if request.method == 'POST':
     form = comment2(request.POST, instance=eachProduct)
     form = comment2(request.POST, request.FILES)
     if form.is_valid():
        name = request.user.username
        body = form.cleaned_data['body']
        img =  form.cleaned_data.get('image')
        c =  models.Hello2(name=name,image=img ,post= eachProduct, body=body, date_added=datetime.now())
        c.save()
        messages.success(request,'comment successfully')
        return redirect('detailss',id = pk)
         
        
  else :
         form = comment2(request.POST)
  return render(request, 'projectApp/addcomment2.html',{'form': form})

def addcomment3(request,pk):
  eachProduct = models.Add3.objects.get(id=pk)
  cot = models.Hello3.objects.filter(pk=pk).last()
  form = comment3(instance=eachProduct)
  if request.method == 'POST':
     form = comment3(request.POST, instance=eachProduct)
     form = comment3(request.POST, request.FILES)
     if form.is_valid():
        name = request.user.username
        body = form.cleaned_data['body']
        img =  form.cleaned_data.get('image')
        c =  models.Hello3(name=name,image=img ,post= eachProduct, body=body, date_added=datetime.now())
        c.save()
        messages.success(request,'comment successfully')
        return redirect('details3',id = pk)
         
        
  else :
         form = comment3(request.POST)
  return render(request, 'projectApp/addcomment3.html',{'form': form})

def about (request) :
    return HttpResponse("about Geeks")
def search (request) :
    if request.method == 'GET':
        search = request.GET.get('search')
        post = models.Add.objects.all().filter(title=search)
    return render ( request,'projectApp/search.html',{'post':post})

def contact (request) :
    return HttpResponse("contact Geeks")
def Update (request,pk) :
    pk  = models.Add.objects.get(pk=pk)
    if request.method == 'POST':
     form = GeeksForm(request.POST,instance=pk)
     if form.is_valid():
        form.save()
        messages.success(request,'post have  Updated successfully')
        return redirect('/posts') 
          
    else :
         form = GeeksForm(instance=pk)
         return render ( request,'projectApp/Update.html',{'form' : form})
def Update2 (request,pk) :
    pk  = models.Add2.objects.get(pk=pk)
    if request.method == 'POST':
     form = GeeksForm2(request.POST,instance=pk)
     if form.is_valid():
        form.save()
        messages.success(request,'post have  Updated successfully')
        return redirect('/posts2') 
          
    else :
         form = GeeksForm2(instance=pk)
         return render ( request,'projectApp/Update2.html',{'form' : form})
def Update3 (request,pk) :
    pk  = models.Add3.objects.get(pk=pk)
    if request.method == 'POST':
     form = GeeksForm3(request.POST,instance=pk)
     if form.is_valid():
        form.save()
        messages.success(request,'post have  Updated successfully')
        return redirect('/posts3') 
          
    else :
         form = GeeksForm3(instance=pk)
         return render ( request,'projectApp/Update3.html',{'form' : form})
def delete (request,pk) :
    info  = models.Add.objects.get(pk=pk)
    info.delete()
    messages.success(request,'post have  Deleted successfully')
    return redirect('/posts')
def delete2 (request,pk) :
    info  = models.Add2.objects.get(pk=pk)
    info.delete()
    messages.success(request,'post have  Deleted successfully')
    return redirect('/posts2')
def delete3 (request,pk) :
    info  = models.Add3.objects.get(pk=pk)
    info.delete()
    messages.success(request,'post have  Deleted successfully')
    return redirect('/posts3')
def delete_comment(request, pk):
    comment = models.Hello.objects.filter(pk=pk).last()
    product_id = comment.post.id
    comment.delete()
    return redirect('details', id=comment.post.id)
def delete_comment2(request, pk):
    comment2 = models.Hello2.objects.filter(pk=pk).last()
    product_id = comment2.post.id
    comment2.delete()
    return redirect('detailss', id=comment2.post.id)
def delete_comment3(request, pk):
    comment2 = models.Hello2.objects.filter(pk=pk).last()
    product_id = comment2.post.id
    comment2.delete()
    return redirect('details3', id=comment2.post.id)
   
