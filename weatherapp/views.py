#this is views.py file
from django.shortcuts import render
from rest_framework import viewsets
from .models import wapp
from .serializers import wappserializer

class wappview(viewsets.ModelViewSet):
    queryset=wapp.objects.all()
    serializer_class = wappserializer


def home(request):
    import requests
    
    if request.method=="POST":
        searched=request.POST['search_place']
        api_data=requests.get("http://api.openweathermap.org/data/2.5/weather?appid=ENTER_YOUR_API_KEY_HERE="+searched)
        try:
            api=api_data.json()
            api_place=api['name']
            api_temp=round(api['main']['temp']-273,2)
            api_desc=api['weather'][0]['description'].capitalize()
            api_con=api['sys']['country']
        except KeyError as e:
            api="Error..."
            return render(request,'home.html',{'api':api,'place':searched})
        except NameError as e:
            api="Error..."
            return render(request,'home.html',{'api':api,'place':searched})        
        return render(request,'home.html',{'api':api,'place':api_place,'temp':api_temp,'desc':api_desc,'api_con':api_con})
    else:
        api_data=requests.get("http://api.openweathermap.org/data/2.5/weather?appid=ENTER_YOUR_API_KEY_HERE&q=Bangalore")
        try:
            api=api_data.json()
            api_place=api['name']
            api_temp=round(api['main']['temp']-273,2)
            api_desc=api['weather'][0]['description'].capitalize()
            api_con=api['sys']['country']
        except Excpetion as e:
            api="Error..."
        return render(request,'home.html',{'api':api,'place':api_place,'temp':api_temp,'desc':api_desc,'api_con':api_con})

def about(request):
    return render(request,'about.html',{})

