from . import views
from django.urls import path

urlpatterns = [
    path('',views.home,name="home"),
    path('about.html',views.about,name="about"),
    
]