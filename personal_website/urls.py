"""personal_website URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from .views import home_view

from blog.views import blog_list_view, blog_detail_view
from showcase_project.views import project_list_view, project_detail_view


urlpatterns = [
    path('', home_view, name='home'),
    path('admin/', admin.site.urls),
    path('blog/', blog_list_view, name='blog'),
    path('blog_detail_view/', blog_detail_view, name='blog_detail_view'),
    path('project_list_view/', project_list_view, name='project_list_view'),
    path('project_detail_view/', project_detail_view, name='project_detail_view'),  
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
