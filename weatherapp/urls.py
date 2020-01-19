from . import views
from django.urls import path,include
from rest_framework import routers

router=routers.DefaultRouter()
router.register('wapp',views.wappview)


urlpatterns = [
    path('',views.home,name="home"),
    path('about.html',views.about,name="about"),
    path('route',include(router.urls)),
    
]