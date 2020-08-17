from django.shortcuts import render


def blog_list_view(request):
    context = {}

    return render(request, 'blog/list.html', context)


def blog_detail_view(request):
    context = {}

    return render(request, 'blog/detail.html', context)