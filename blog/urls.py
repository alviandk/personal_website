from django.urls import path

from . import views


app_name = 'blog'
urlpatterns = [
    path('', views.blog_list_view, name='post_list'),
    path('<slug>/', views.blog_detail_view, name='post_detail'),
]