from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout
from django.shortcuts import redirect
from core.models import Profile
from django.contrib import messages


def login_view(request):

    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, f'login was successfull welcome {user.username}')
            return redirect('home')
    else:    
        form = AuthenticationForm(request)
    return render(request, 'authentication/login.html', {'form':form})


def logout_view(request):

    if request.method == "POST":
        logout(request)
        return redirect('home')

    return render(request, 'authentication/logout.html')    


def register_view(request):

    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():

            user = form.save(commit=False)
            form.save()
            messages.success(request, f'registration was successfull welcome {user.username}')

            login(request, user)
            return redirect('home')
        
    else:
        form = UserCreationForm()

    return render(request, 'authentication/register.html', {'form':form})        
