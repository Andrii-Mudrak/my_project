from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.forms import Form
from .forms import SignUpForm

# Create your views here.

def list(request):
    return render(request, 'mainapp/list.html')

def create(request):
    return render(request, 'mainapp/create.html')

def comment(request):
    return render(request, 'mainapp/comment.html')

def look(request):
    return render(request, 'mainapp/look.html')

def done(request):
    return render(request, 'mainapp/done.html')

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user, password=raw_password)
            login(request, user)
            return redirect('/')
    else:
        form = SignUpForm()
    return render(request, 'mainapp/signup.html', {'form': form})
