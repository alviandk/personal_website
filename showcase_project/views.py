from django.shortcuts import render

from .models import Project


def project_list_view(request):
    context = {}

    context['project_list'] = Project.objects.all()

    return render(request, 'project/list.html', context)


def project_detail_view(request, slug):
    context = {}

    return render(request, 'project/detail.html', context)