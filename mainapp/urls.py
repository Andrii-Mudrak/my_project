from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.home),
    path('', include('django.contrib.auth.urls')),
    path('product/<id>/', views.product),
    path('home', views.home),
    path('list_p', views.list_p),
    path('profile', views.profile),
    path('create', views.create, name='create'),
    path('comment/<id>/', views.comment),
    path('look/<id>/', views.look),
    path('done', views.done),
    path('signup', views.signup, name='signup'),
    path('restore/<id>/', views.restore),
    path('delete/<id>/', views.delete),
    path('revised/<id>/', views.revised),
    path('about', views.about),
    path('delete_account', views.delete_account),
    path('change_account', views.change_account),
]
