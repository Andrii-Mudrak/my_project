from django.urls import path, include
from . import views
from .views import HomeView
# from django.views.generic import TemplateView

urlpatterns = [
    path('', HomeView.as_view()),
    path('', include('django.contrib.auth.urls')),
    path('product', views.product),
    # path('home', views.home),
    path('list', views.list),
    path('create', views.create),
    path('comment', views.comment),
    path('look', views.look),
    path('done', views.done),
    path('signup', views.signup, name='signup'),
    path('', HomeView.as_view(), name='home'),
]
