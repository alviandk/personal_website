from django.urls import path

from . import views


app_name = 'showcase_project'
urlpatterns = [
    path('', views.project_list_view, name='project_list'),
    path('<slug>/', views.project_detail_view, name='project_detail'),
]