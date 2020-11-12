from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Comment, Product, Responce, Profile
# Create your views here.


def home(request):
    count = User.objects.count()
    return render(request, 'mainapp/home.html', {'count': count})


def list(request):
    count = User.objects.count()
    return render(request, 'mainapp/list.html', {'count': count})


def create(request):
    count = User.objects.count()
    return render(request, 'mainapp/create.html', {'count': count})


def comment(request):
    # count = User.objects.count()
    com = Comment.objects.all()
    return render(request, 'mainapp/comment.html', {'title': 'Коментарccc', 'comm': com})


def look(request):
    count = User.objects.count()
    return render(request, 'mainapp/look.html', {'count': count})


def done(request):
    count = User.objects.count()
    return render(request, 'mainapp/done.html', {'count': count})


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'mainapp/home.html')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})
