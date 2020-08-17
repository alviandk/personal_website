from django.shortcuts import render


def project_list_view(request):
    context = {}

    return render(request, 'project/list.html', context)


def project_detail_view(request):
    context = {}

    return render(request, 'project/detail.html', context)