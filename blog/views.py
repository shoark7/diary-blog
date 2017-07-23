from django.conf.urls import url
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.template import loader, RequestContext

from .forms import WriteForm
from .models import Category, Post


def index(request):
    latest_posts = Post.objects.all()[:5]
    context = {'latest_posts': latest_posts}
    return render(request, 'blog/index.html', context)


def write(request):
    if request.method == 'POST':
        form = WriteForm(request.POST)
        if form.is_valid():
            category = form.cleaned_data['categories']
            text = form.cleaned_data['text']
            title = form.cleaned_data['title']
            writer = request.user
            post = Post.objects.create(categories=category, text=text,
                                      title=title, writer=writer)
            post.save()
            return render(request, 'blog/index.html')
        else:
            pass
    else:
        form = WriteForm()
    return render(request, 'blog/write_post.html', {'form': form})


def list(request):
    all_lists = Post.objects.all()
    context = {'posts': all_lists}

    template = loader.get_template('blog/list.html')
    return HttpResponse(template.render(context))


def detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/detail.html', {'post': post})
