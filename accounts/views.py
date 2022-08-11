from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
import accounts
from .forms import LoginForm

# Create your views here.

def login_view(request):
    if request .method == 'POST':
        form = LoginForm(request.POST)
        user = authenticate(
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('pasword')
        )
    return render(request, 'accounts/login.html' , {'form' })

def logout_view(request):
    logout(request)
    return redirect('index')