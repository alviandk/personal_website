from django.contrib import admin

from .models import Description, PersonalInformation, ProfilePicture


admin.site.register(Description)
admin.site.register(PersonalInformation)
admin.site.register(ProfilePicture)