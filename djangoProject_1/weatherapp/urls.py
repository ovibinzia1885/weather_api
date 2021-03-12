
from django.urls import path
from .views import CityWeaterView,City_delete
from weatherapp import views
app_name="weatherapp"
urlpatterns = [
    path('',CityWeaterView,namespace='city_weather'),
    path('remove/<city_name>/',City_delete,name='city_delete'),



]
