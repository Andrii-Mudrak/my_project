from django.shortcuts import render, redirect
# from django.views.generic import ListView, DetailView
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Comment, Product, Responce, Profile
from .forms import SignUpForm, ProductForm, ProfileForm
from django.contrib.auth.decorators import login_required

# from django.contrib.auth.decorators import login_required
# from django.db import transaction
# Create your views here.


def home(request):
    count = User.objects.count()
    prod = Product.objects.all()
    prof = User.objects.all()
    return render(request, 'mainapp/home.html', {'title': 'перелік', 'prod': prod, 'prof': prof, 'count': count})


def list(request):
    count = User.objects.count()
    return render(request, 'mainapp/list.html', {'count': count})


def create(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        # User = request.user.username
        if form.is_valid() and request.user.is_authenticated:
            # profile = Profile.objects.filter(user=request.user).values('id')
            print(request.user, '******', request.user.username)
            profile = Profile.objects.filter(user=request.user.username).value('name')
            print(profile, '****')
            Product.author = profile.get('user')
            print(profile, '****', Product.author)
            # print(profile, '*****', form.author)
            form.save()
        return render(request, 'mainapp/home.html'  )
    else:
        form = ProductForm()
        return render(request, 'mainapp/create.html', {'form': form})


def comment(request):
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
        form = SignUpForm(request.POST)
        profile_form = ProfileForm(request.POST)
        if form.is_valid() and profile_form.is_valid():
            user = form.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
        context = {'form': form, 'profile_form': profile_form}
        return render(request, 'mainapp/home.html')
    else:
        form = SignUpForm()
        profile_form = ProfileForm()
        return render(request, 'mainapp/signup.html', {'form': form, 'profile_form': profile_form})


def product(request):
    return render(request, 'mainapp/product.html')


def profile(request):
    # return render(request, 'mainapp/home.html')
    if request.method == 'POST':
        form = ProfileForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/home')
    else:
        form = ProfileForm()
        return render(request, 'mainapp/profile.html', {'form': form})
