from django.contrib.auth import logout
from django.shortcuts import render, redirect
from .models import Product, Profile, Comment
from .forms import SignUpForm, ProductForm, ProfileForm, CommentForm
from django.contrib.auth.decorators import login_required
from datetime import datetime
from django.shortcuts import get_object_or_404
import logging
from django.views.generic.base import TemplateView


logging.basicConfig(filename='logger.log', level=logging.DEBUG)
logger = logging.getLogger()


def home(request):
    """Домашня сторінка"""
    # logout(request)
    prod = Product.objects.all()
    return render(request, 'mainapp/home.html', {'prod': prod})


@login_required()
def list_p(request):
    """Перелік об'яв, створених користувачем який залогінений"""
    prof_id = Profile.objects.get(user=request.user).id
    prod = Product.objects.filter(author_id=prof_id)
    # prod = Product.objects.filter(author__id=request.user.id)
    logger.info(f"користувач переглядає {request.user.id}")
    return render(request, 'mainapp/list.html', {'prod': prod})


@login_required()
def create(request):
    """Створення оголошення"""
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid() and request.user.is_authenticated:
            prod = form.save(commit=False)
            prod.is_active = 1
            prod.author = Profile.objects.get(user=request.user)
            prod.save()
            prod.image = form.instance
        return redirect('/home')
    else:
        form = ProductForm()
        return render(request, 'mainapp/create.html', {'form': form})


@login_required()
def comment(request, id):
    """Запис коментаря до певного оголошення"""
    prod = Product.objects.get(id=id)
    logger.info(f"comment {prod}")
    comm = Comment.objects.filter(product_id=id)
    return render(request, 'mainapp/comment.html', {'comm': comm, 'prod': prod})


# @login_required()
# def look(request, id):
#     """Перегляд оголошення"""
#     user_list = get_object_or_404(Product, id=id)
#     if request.method == 'POST' and request.user.is_authenticated:
#         form = CommentForm(request.POST)
#         if form.is_valid():
#             comm = form.save(commit=False)
#             comm.user_id = Profile.objects.get(user=request.user)
#             comm.product_id = Product.objects.get(id=id)
#             comm.save()
#         return redirect('/home')
#     else:
#         form = CommentForm()
#     return render(request, 'mainapp/look.html', {'user_list': user_list, 'form': form})


def signup(request):
    """Реєстрація нового користувача в базі"""
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        profile_form = ProfileForm(request.POST)
        if form.is_valid() and profile_form.is_valid():
            user = form.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.is_verified = True
            profile.name = profile.user
            profile.save()
        return redirect('/home')
    else:
        form = SignUpForm()
        profile_form = ProfileForm()
        return render(request, 'mainapp/signup.html', {'form': form, 'profile_form': profile_form})


@login_required()
def product(request,id):
    """Видалення оголошення шляхом зміни атрибуту is_active. Автор оголошення може потім або видалити
    остаточно або відновити."""
    prod = Product.objects.get(id=id)
    prod.is_active = False
    prod.deleted_at = datetime.utcnow()
    prod.save()
    return redirect('/list_p')


@login_required()
def profile(request):
    """Редагування існуючого профілю: Ім'я, прізвище, електронна пошта та телефон"""
    if request.method == 'POST':
        form = ProfileForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/home')
    else:
        form = ProfileForm()
        return render(request, 'mainapp/profile.html', {'form': form})


@login_required()
def done(request):
    """Відображення оголошень які було видалено автором. Їх  можливо за бажання автора
    або відновити або видалити остаточно"""
    prod = Product.objects.filter(author__user=request.user, is_active=False).all()
    print('done -- ', request.method)
    # print(list(prod))
    return render(request, 'mainapp/done.html', {'prod': prod})


@login_required()
def restore(request, id):
    """Відновлення раніше видалених повідомлень"""
    prod = Product.objects.get(id=id)
    prod.is_active = True
    prod.save()
    return redirect('/done')


@login_required()
def delete(request, id):
    """Остаточне видалення повідомлень"""
    print('delete---', request.method)
    if request.method == "POST":
        Product.objects.filter(id=id).delete()
    return redirect('/done')


@login_required()
def revised(request, id):
    """Зміна статусу коментаря до оголошення на <<переглянуте>>"""
    comm = Comment.objects.get(id=id)
    comm.revised = True
    comm.save()
    return redirect('/home')


@login_required()
def about(request):
    """Відображення відомостей про користувача який залогінений з пропозицією
    або змінити дані або видалити акаунт"""
    # prof_id = Profile.objects.get(user=request.user).id
    # prof = Profile.objects.filter(id=prof_id)s
    prof = Profile.objects.filter(id=request.user.id)
    return render(request, 'mainapp/about.html', {'prof': prof})


@login_required()
def delete_account(request):
    """Видалення акаунту"""
    request.user.is_active = 0
    request.user.save()
    logout(request)
    return redirect('/home')


@login_required()
def change_account(request, id=int):
    """"Зміна даних акаунту"""
    logger.info(f"користувач {request.user}")
    if request.method == 'POST' and request.user.is_authenticated:
        form = ChangeAccountForm(request.POST)
        if form.errors:
            logger.info(f'!!!!! помилка {form.errors}')
        if form.is_valid():
            prof_id = Profile.objects.get(user=request.user).id
            prof = Profile.objects.get(id=prof_id)
            prof.first_name = form['first_name'].value()
            prof.last_name = form['last_name'].value()
            prof.email = form['email'].value()
            prof.phone = form['phone'].value()
            prof.updated_at = datetime.utcnow()
            prof.save()
            logout(request)
        return redirect('/home')
    else:
        form = ChangeAccountForm()
    return render(request, 'mainapp/change_account.html', {'form': form})


class DetailedProduct(TemplateView):
    template_name = "mainapp/look/<pk>.html"

    # prod = Product.objects.all()
    # print("***-", prod)

    def __init__(self, user):
        prod = Product.objects.get(author=user).all()
        print('sdfsdfsdfsdfsdf')
        return render(request, 'mainapp/home.html', {'prod': prod})

    def dispatch(request, user):
        return print(user)

    def get_context_data(request, user):
        context = super(DetailedProduct, self).get_context_data(**kwargs)
        # context['user.id'] = Product.objects.get(author=user)
        print(1)
        return print(context)

    def get_instance(pk):
        prod = Product.objects.get(id=pk)
        # return get_object_or_404(Product, pk=pk)
        # return render(request, template_name=template_name, {'prod': prod})


    def get(self, request, pk):
        prod = super().get(self, request, id=pk)
        print(prod, pk)
        # return render(request, 'mainapp/home.html', {'prod': prod})
        return print(pk, prod)


    @login_required()
    def post(self, request, pk):
        pass

    @login_required()
    def delete(self, request, pk):
        pass
