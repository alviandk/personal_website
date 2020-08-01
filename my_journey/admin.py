from django.contrib import admin

from .models import (
    Accomplishment, Certificate, Company, 
    Competition, Experience, TechStack
)


admin.site.register(Accomplishment)
admin.site.register(Company)
admin.site.register(Experience)
admin.site.register(Competition)
admin.site.register(Certificate)
admin.site.register(TechStack)
