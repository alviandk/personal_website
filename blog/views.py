from django.shortcuts import render

from .models import Post


def blog_list_view(request):
    context = {}

    blog_posts = Post.objects.filter(status='PUBLISHED')
    context['blog_posts'] = blog_posts

    return render(request, 'blog/list.html', context)


def blog_detail_view(request, slug):
    context = {}

    post = Post.objects.get(slug=slug)
    context['post'] = post

    return render(request, 'blog/detail.html', context)