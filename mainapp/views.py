from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import Product, Profile
from .forms import SignUpForm, ProductForm, ProfileForm, CommentForm
from django.contrib.auth.decorators import login_required
from datetime import datetime
# Create your views here.


def home(request):
    count = User.objects.count()
    prod = Product.objects.all().filter(is_active=True)
    prof = User.objects.all()
    return render(request, 'mainapp/home.html', {'title': 'перелік', 'prod': prod, 'prof': prof, 'count': count})


def list_p(request):
    prof_id = Profile.objects.get(user=request.user).id
    prod = Product.objects.all().filter(author_id=prof_id)
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


def comment(request):
    prod = request.GET.get('')
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid() and request.user.is_authenticated:
            comm = form.save(commit=False)
            comm.user_id = Profile.objects.get(user=request.user)
            print(comm, comm.user_id)
            comm.product_id = prod
            comm.save()
        return render(request, 'mainapp/home.html')
    else:
        form = CommentForm()
        return render(request, 'mainapp/comment.html', {'form': form})


@login_required()
def look(request, id='1'):
    user_list = Product.objects.get(id=id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid() and request.user.is_authenticated:
            comm = form.save(commit=False)
            comm.user_id = Profile.objects.get(user=request.user)
            comm.product_id = Product.objects.get(id=id)
            comm.save()
        return render(request, 'mainapp/home.html')
    else:
        form = CommentForm()
    return render(request, 'mainapp/look.html', {'user_list': user_list, 'form': form})


# def done(request):
#     count = User.objects.count()
#     return render(request, 'mainapp/done.html', {'count': count})


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


def product(request,id='1'):
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
    prod = Product.objects.all().filter(author_id=prof_id, is_active=False)
    return render(request, 'mainapp/done.html', {'prod': prod})


def restore(request,id='1'):
    prod = Product.objects.get(id=id)
    # prod.delete() # видалення запису з бази даних повністю
    prod.is_active = True
    prod.save()
    return render(request, 'mainapp/home.html')


def delete(request,id='1'):
    prod = Product.objects.get(id=id)
    prod.delete() # видалення запису з бази даних повністю
    prod.save()
    return render(request, 'mainapp/home.html')