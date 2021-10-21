from django.shortcuts import redirect, render
from django.http import HttpResponse 
from django.contrib.auth.models import User
from user.models import Contactus
from django.contrib.auth.hashers import make_password
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
#from django.contrib.messages import constants as messages


# Create your views here.

def codelabs(request):
    if request.method == "GET":
        return render(request,'user/home.html')



def signup(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method =="GET":
        return render(request,'user/signup.html')


    first_name=request.POST['first_name']
    last_name=request.POST['last_name']
    email=request.POST['email']
    username=request.POST['username']
    password=request.POST['password']

    try:
        user=User.objects.get(username=username)
        messages.info(request, 'Username Already Taken')
        return redirect('signup')
     
    except User.DoesNotExist :
        user=User(
            first_name=first_name,
            last_name=last_name,
            email=email,
            username=username,
            password=make_password(password),  #fro login to be happened we need hashed password and not raw pasowrd i.e why we use make_password
            )

        user.save() 
        login(request,user) 
        messages.success(request, "You Have Signup Successfully")    
        return redirect('home')


def home(request):
    print(request.user)
    return render(request,'user/home.html')


def login_view(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == "GET":
        return render(request,'user/login.html')

    username = request.POST['username']
    password = request.POST['password']

    user = authenticate(request, username=username, password=password)

    if user is not None:
        login(request, user)
        messages.success(request,"Welcome Back")
        return render(request,'user/home.html')
    else:
        messages.info(request, 'please enter valid credentials')
        return redirect('login')

def logout_view(request):
    logout(request) 
    messages.info(request,"You are logged out")
    return redirect('home')



@login_required(login_url='login') 
def aboutus(request):
    return render(request, 'user/aboutus.html')
    


@login_required(login_url='login') 
def courses(request):
    return render(request,'user/courses.html')



@login_required(login_url='login') 
def contactus(request):
    if request.method == "GET":
        return render(request,'user/contactus.html')

    email=request.POST['email'] 
    query=request.POST['query']
    suggestion=request.POST['suggestion']
    
    user=Contactus(email=email,query=query,suggestion=suggestion)

    user.save()
    messages.success(request," Your Query Sent Successfully")
    return redirect('contactus')