from django.conf.urls import url
from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

from .models import Category, Post


def index(request):
    latest_posts = Post.objects.all()[:5]
    context = {'latest_posts': latest_posts}


    template = loader.get_template('blog/index.html')
    return HttpResponse(template.render(context))
