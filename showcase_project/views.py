from django.shortcuts import render

from .models import Project


def project_list_view(request):
    context = {}

    context['project_list'] = Project.objects.all()

    return render(request, 'project/list.html', context)


def project_detail_view(request, slug):
    context = {}

    context['project'] = Project.objects.get(slug=slug)

    return render(request, 'project/detail.html', context)