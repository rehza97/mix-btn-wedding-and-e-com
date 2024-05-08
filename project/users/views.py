from django.http import HttpResponse
from django.shortcuts import render , redirect
from django.contrib.auth import authenticate , login , logout
from django.contrib.auth import get_user_model
from django.contrib import messages
from .models import *
from .forms import *
# Create your views here.



# def regFirstTypoeUser(request):
#     if request.method == 'POST':
#         form = ResisterUserForm(request.POST)
       
       
#         if form.is_valid():
#             var = form.save(commit=False)
#             var.save()
#             messages.success(request, 'Account Created Successfully')
#             return redirect('users:login_user')
#         else:
#             messages.warning(request, 'something went wrong')
#             return redirect('users:reg')
#     else:
#         form = ResisterUserForm()
#         context = {
#             'form': form
#         }
#         return render(request, 'users/register.html', context) 
    
def register_user(request):
    User = get_user_model()

    if request.method == 'POST':
        form = ResisterUserForm(request.POST)
    

        if form.is_valid():
            user =form.save(commit=False)
            user.email = user.username
            user.save()
            return redirect('users:login')
    else:
        form = ResisterUserForm()
    context = {'form': form}
    return render(request, 'users/login-register.html', context)
    
    
def login_user(request):
    if request.method == 'POST':
        email = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=email, password=password)
        if user is not None and user.is_active:
            login(request, user)
      
            return HttpResponse('hello')

        else:
            messages.error(request,'something went wrong')
            return redirect('users:login')
    else:
        form = ResisterUserForm()
        context = {'form': form}
        return render(request, 'users/login-register.html', context)
    
def logout_user(request):
    logout(request)
    messages.info(request , '3awd walilana ki tahna')
    return redirect('users:login')
