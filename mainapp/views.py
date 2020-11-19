from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Comment, Product, Responce, Profile
from .forms import SignUpForm
# Create your views here.

#
# def home(request):
#     count = User.objects.count()
#     prod = Product.objects.all()
#     return render(request, 'mainapp/home.html', {'title': 'перелік', 'prod': prod, 'count': count})
class HomeView(TemplateView):
    # model = Product
    template_name = "mainapp/home.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Needed_Product'] = Product.objects.all()[:5]
        return context


def list(request):
    count = User.objects.count()
    return render(request, 'mainapp/list.html', {'count': count})


def create(request):
        return render(request, 'mainapp/home.html')
    # else:
    #     form = SignUpForm()
    # # return render(request, 'registration/signup.html', {'form': form})
    # return render(request, 'mainapp/create.html', {'count': count})


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
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
        return render(request, 'mainapp/home.html')
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})


def product(request):
    return render(request, 'mainapp/product.html')
