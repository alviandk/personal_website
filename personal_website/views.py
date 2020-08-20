from django.shortcuts import render

from about_me.models import Description, PersonalInformation, ProfilePicture
from blog.models import Post
from my_journey.models import Competition, Experience, TechStack
from education.models import School
from showcase_project.models import App


def home_view(request):
    context = {}
    
    context['description'] = Description.objects.first()
    context['personal_information'] = PersonalInformation.objects.first()
    context['profile_picture'] = ProfilePicture.objects.first()

    context['experiences'] = Experience.objects.all().order_by('-start_date')
    context['competitions'] = Competition.objects.all()
    context['tech_stacks'] = TechStack.objects.all()

    context['schools'] = School.objects.all()

    return render(request, 'home.html', context)