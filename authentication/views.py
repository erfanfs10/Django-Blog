from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
from django.shortcuts import redirect
from django.contrib import messages
from django.utils.translation import gettext_lazy as _
from authentication.forms import CustomUserCreationForm




def login_view(request):

    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            msg = _('login was successfull welcome %(user)s' ) % {'user': user.username}
            messages.success(request, msg)
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
        form = CustomUserCreationForm(request.POST)

        if form.is_valid():

            user = form.save(commit=False)
            form.save()
            msg = _('registration was successfull welcome %(user)s' ) % {'user': user.username}
            messages.success(request, msg)
            login(request, user)

            subject = 'Welcome to My Site!'
            message = f'Hi {user.username},\n\nThanks for registering on My Site!'
            user.send_welcome_email(subject, message) # send welcome email to user

            return redirect('home')
        
    else:
        form = CustomUserCreationForm()
        
    return render(request, 'authentication/register.html', {'form':form})        
