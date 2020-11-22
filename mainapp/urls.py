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
    path('create', views.create, name='create'),
    path('comment', views.comment),
    # path('look', HomeView.as_view(template_name="mainapp/home.html")),
    path('done', views.done),
    path('signup', views.signup, name='signup'),
]
