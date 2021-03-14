
from django.urls import path
from django.urls import path
from .views import CityWeaterView, City_delete

app_name='weatherapp'

urlpatterns = [
    path('',CityWeaterView,name='home'),
    path('remove/<city_name>/', City_delete, name='City_remove')



]
