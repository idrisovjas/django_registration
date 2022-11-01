from django.shortcuts import render, redirect
from django.contrib.auth import login,logout,authenticate
from .models import CustomUser

def log_in(request):
    if request.method=='POST':
        username = request.POST.get('username',None)
        password = request.POST.get('password',None)
        user = authenticate(username=username,password=password)
        if user:
            login(request,user)
            return redirect('home')
    return render(
        request=request,
        template_name='login.html'
    )

def register(request):
    if request.method=='POST':
        first_name = request.POST.get('first_name',None)
        last_name = request.POST.get('last_name',None)
        email = request.POST.get('email',None)
        password1 = request.POST.get('password1',None)
        password2 = request.POST.get('password2',None)
        username = request.POST.get('username',None)
        print(request.POST)
        user = CustomUser.objects.filter(
            email = email
        )
        if user:
            return redirect('login')
        if password2==password1:
            user = CustomUser.objects.create(
                first_name = first_name,
                last_name = last_name,
                username=username,
                email = email,
                password=password1
            )
            user.set_password(password1)
            user.save()
            if user:
             return redirect('login')

    return render(
        request = request,
        template_name='register.html'
    )

def log_out(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect('login')