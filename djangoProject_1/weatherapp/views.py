
from django.shortcuts import render
import requests
from .models import City
from.forms import CityForm
def CityWeaterView(request):
    url = "http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=41f97db19b30b5de5b77ee7a81b313f1"

    if request.method == 'POST':
        form=CityForm(request.POST)
        form.save()
    form=CityForm()
    weather_data=[]
    city= City.objects.all()
    for p in city:
        r =requests.get(url.format(p)).json()
        city_weather={
            'city':p.name,
            'temperature': r['main']['temp'],
            'description': r['weather'][0]['description'],
            'icon': r['weather'][0]['icon'],
        }
        weather_data.append(city_weather)
        print(weather_data)
    context={
        'weather_data':city_weather,
        'form':form,

    }
    return  render(request,'weather.html',context)
