from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name = 'index'),
    path('about', views.about, name = 'about'),
    path('index.html', views.index, name = 'home'),
    path('project', views.project, name = 'project')
   
]