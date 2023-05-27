from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponse

# Create your views here.
def HomePage(request):
    return render(request,'auth_system/index.html', {})

def Register(request):
    if request.method =='POST':
        username=request.POST.get('username')
        last_name = request.POST.get('last_name')
        email=request.POST.get('email')
        password=request.POST.get('pwd')
        
        if User.objects.filter(username=username).exists():
            error_message = 'Username already exists. Please choose a different username.'
            return render(request, 'auth_system/register.html', {'error_message': error_message})

        new_user = User.objects.create_user(username=username,last_name=last_name,email=email,password=password)
        new_user.first_name=username
        new_user.last_name=last_name

        new_user.save()
        return redirect('login-page')


    return render(request,'auth_system/register.html', {})

def  Login(request):
    if request.method =='POST':
        username=request.POST.get('fname')
        password=request.POST.get('pwd')
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('home-page')
        else:
            return HttpResponse("error. the user does not exist")



    return render(request,'auth_system/login.html', {})
