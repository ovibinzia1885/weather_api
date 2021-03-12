
from django.urls import path
from .views import CityWeaterView
from weatherapp import views
# app_name="weatherapp"
urlpatterns = [
    path('',views.CityWeaterView,name="weatherdetails")


]
