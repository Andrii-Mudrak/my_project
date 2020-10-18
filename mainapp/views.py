from django.shortcuts import render


# Create your views here.

def list(request):
    return render(request, 'mainapp/list.html')

def create(request):
    return render(request, 'mainapp/create.html')

def comment(request):
    return render(request, 'mainapp/comment.html')

def look(request):
    return render(request, 'mainapp/look.html')

def done(request):
    return render(request, 'mainapp/done.html')

