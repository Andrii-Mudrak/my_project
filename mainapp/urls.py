from django.urls import path, include
from . import views
# from .views import ArticleDetailView
# from django.views.generic import TemplateView

urlpatterns = [
    path('', views.home),
    path('', include('django.contrib.auth.urls')),
    path('product', views.product),
    path('home', views.home),
    path('list', views.list),
    path('profile', views.profile),
    path('create', views.create, name='create'),
    path('comment', views.comment),
    path('look/<id>/', views.look),
    path('done', views.done),
    path('signup', views.signup, name='signup'),
]
