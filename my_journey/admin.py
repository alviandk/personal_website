from django.contrib import admin

from .models import Accomplishment, Company, Experience


admin.site.register(Accomplishment)
admin.site.register(Company)
admin.site.register(Experience)