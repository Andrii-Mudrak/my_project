from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home),
    path('', include('django.contrib.auth.urls')),
    path('home', views.home),
    path('list', views.list),
    path('create', views.create),
    path('comment', views.comment),
    path('look', views.look),
    path('done', views.done),
    path('signup', views.signup, name='signup'),
]