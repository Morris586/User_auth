from django.shortcuts import render, redirect
from .forms import RegisterForm, PostForm
from django.contrib.auth import login as auth_login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required 

@login_required(login_url="/login")
def home(request):
    return render(request, 'main/home.html')

@login_required(login_url="/login")
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('home') 
    else:
        form = PostForm()

    return render(request, 'main/create_post.html', {'form': form})



def sign_up(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user= form.save()
            auth_login(request, user)
            return redirect('home')
    else:
        form= RegisterForm()
    return render(request, 'registration/sign_up.html', {'form': form})


def user_login(request):
   if request.method == 'POST':
       form = AuthenticationForm(data=request.POST)
       if form.is_valid():#log the user in
           user = form.get_user()
           auth_login(request, user)
           return redirect('home')
   else:
       form= AuthenticationForm()

   return render(request,'registration/login.html', {'form':form} )