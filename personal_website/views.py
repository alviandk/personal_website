from django.shortcuts import render

from about_me.models import Description, PersonalInformation, ProfilePicture
from my_journey.models import Experience
from education.models import School


def home_view(request):
    context = {}
    
    context['description'] = Description.objects.first()
    context['personal_information'] = PersonalInformation.objects.first()
    context['profile_picture'] = ProfilePicture.objects.first()

    context['experiences'] = Experience.objects.all()

    context['schools'] = School.objects.all()

    return render(request, 'home.html', context)