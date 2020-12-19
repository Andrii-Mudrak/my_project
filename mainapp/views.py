from django.shortcuts import render, redirect
# from django.views.generic import ListView, DetailView
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Comment, Product, Responce, Profile
from .forms import SignUpForm, ProductForm, ProfileForm, CommentForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404

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
        if form.is_valid() and request.user.is_authenticated:
            prod = form.save(commit=False)
            prod.is_active = 1
            prod.author = Profile.objects.get(user=request.user)
            prod.save()
        return render(request, 'mainapp/home.html')
    else:
        form = ProductForm()
        return render(request, 'mainapp/create.html', {'form': form})


def comment(request):
    # print(Product.objects.get(id))
    prod = get_object_or_404(Product, id)
    print('*****', prod)
    if request.method == 'POST':
        form = CommentForm(request.POST)

        if form.is_valid() and request.user.is_authenticated:
            comm = form.save(commit=False)
            comm.user_id = Profile.objects.get(user=request.user)
            print(comm, comm.user_id)
            comm.product_id = prod.object.get(user=request.user)
            comm.save()
        return render(request, 'mainapp/home.html')
    else:
        form = CommentForm()
        return render(request, 'mainapp/comment.html', {'form': form})


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
            profile.verified = 1
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
