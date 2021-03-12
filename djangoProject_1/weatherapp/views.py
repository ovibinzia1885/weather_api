
from django.shortcuts import render, get_object_or_404, redirect
import requests
from .models import City
from.forms import CityForm
def CityWeaterView(request):
    url = "http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=41f97db19b30b5de5b77ee7a81b313f1"
    errmsg=''
    msg=''
    msclass=''
    if request.method == 'POST':
        form=CityForm(request.POST)
        if form.is_valid():
            new_city=form.cleaned_data['name']
            city_count=City.objects.filter(name=new_city).count()
            if city_count==0:
                r=requests.get(url.format(new_city)).json()
                if r['cod']==200:
                    form.save()
                else:
                    errmsg="the city is not in the world"
            else:
                errmsg="Already city is add to database"
        if errmsg:
            msg=errmsg
            msclass='is-danger'
        else:
            msg="the city is added"
            msclass='is-success'

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
        'msg':msg,
        'msclass':msclass,

    }
    return  render(request,'weather.html',context)

def City_delete(request,city_name):
    city=get_object_or_404(City,name=city_name)
    city.delete()
    return redirect('city_weather')
