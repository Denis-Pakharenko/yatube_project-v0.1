from multiprocessing import context
from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

# Create your views here.

def index(request):
    template = 'posts/index.html'
    posts = Post.objects.order_by('-pub_date')[:10]
    context = {
        'posts': posts,
    }
    return render(request, template, context)

def group_posts(request):
    template = 'posts/group_list.html'
    context = {'text': 'Здесь будет информация о группах проекта Yatube'}
    return render(request, template, context)