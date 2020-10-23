from django.urls import path
from . import views

urlpatterns = [
    path('', views.list),
    path('list', views.list),
    path('create', views.create),
    path('comment', views.comment),
    path('look', views.look),
    path('done', views.done),
    path('signup', views.signup),
]