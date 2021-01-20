from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import Product, Profile, Comment
from .forms import SignUpForm, ProductForm, ProfileForm, CommentForm
from django.contrib.auth.decorators import login_required
from datetime import datetime
from django.shortcuts import get_object_or_404
# Create your views here.


def home(request):
    # count = User.objects.count()
    prod = Product.objects.filter(is_active=True).all()
    prof = Profile.objects.filter(id=prod).all()
    return render(request, 'mainapp/home.html', {'title': 'перелік', 'prod': prod, 'prof': prof})


def list_p(request):
    prof_id = Profile.objects.get(user=request.user).id
    prod = Product.objects.filter(author_id=prof_id)
    # com = Comment.objects.filter(user_id=prof_id).get()
    print(prof_id, prod)
    return render(request, 'mainapp/list.html', {'prod': prod})


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


def comment(request, id=int):
    prod = Product.objects.get(id=id)
    comm = Comment.objects.filter(product_id=id)
    print(prod.id, prod.title, prod.content)
    return render(request, 'mainapp/comment.html', {'comm': comm, 'prod': prod})


@login_required()
def look(request, id=int):
    # user_list = Product.objects.get(id=id)
    user_list = get_object_or_404(Product, id=id)
    if request.method == 'POST' and request.user.is_authenticated:
        form = CommentForm(request.POST)
        if form.is_valid():
            comm = form.save(commit=False)
            comm.user_id = Profile.objects.get(user=request.user)
            comm.product_id = Product.objects.get(id=id)
            comm.save()
        return render(request, 'mainapp/home.html')
    else:
        form = CommentForm()
    return render(request, 'mainapp/look.html', {'user_list': user_list, 'form': form})


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        profile_form = ProfileForm(request.POST)
        print(form.is_valid(), profile_form.is_valid())
        if form.is_valid() and profile_form.is_valid():
            user = form.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.is_verified = True
            profile.name = profile.user
            profile.save()
        # context = {'form': form, 'profile_form': profile_form}
        return render(request, 'mainapp/home.html')
    else:
        form = SignUpForm()
        profile_form = ProfileForm()
        return render(request, 'mainapp/signup.html', {'form': form, 'profile_form': profile_form})


def product(request,id=int):
    prod = Product.objects.get(id=id)
    # prod.delete() # видалення запису з бази даних повністю
    prod.is_active = False
    prod.deleted_at = datetime.utcnow()
    prod.save()
    return render(request, 'mainapp/home.html')


def profile(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/home')
    else:
        form = ProfileForm()
        return render(request, 'mainapp/profile.html', {'form': form})


def done(request):
    prof_id = Profile.objects.get(user=request.user).id
    prod = Product.objects.filter(author_id=prof_id, is_active=False).all()
    return render(request, 'mainapp/done.html', {'prod': prod})


def restore(request,id=int):
    prod = Product.objects.get(id=id)
    # prod.delete() # видалення запису з бази даних повністю
    prod.is_active = True
    prod.save()
    return render(request, 'mainapp/home.html')


def delete(request,id=int):
    prod = Product.objects.get(id=id)
    prod.delete() # видалення запису з бази даних повністю
    prod.save()
    return render(request, 'mainapp/home.html')


def revised(request, id=int):
    comm = Comment.objects.get(id=id)
    comm.revised = True
    comm.save()
    return render(request, 'mainapp/list.html')
