import requests
from django.shortcuts import render
from .models import City
from .forms import CityForm
from rest_framework import viewsets
from .serializers import CitySerializer


def index(request):
    appid = '2ae4982fcaffb015fb0b1b1e2ef16ce7'
    url = 'https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=' + appid

    if (request.method == 'POST'):
        form = CityForm(request.POST)
        form.save()

    form = CityForm()

    cities = City.objects.all()

    all_cities = []

    for city in cities:
        res = requests.get(url.format(city.name)).json()
        city_info = {
            'city': city.name,
            'temp': res["main"]["temp"],
            'wind': res["wind"]["speed"],
            'icon': res["weather"][0]["icon"]
        }
        all_cities.append(city_info)


    context = {'all_info': all_cities, 'form':form}

    return render(request, 'weather/index.html', context)


class CityApi(viewsets.ModelViewSet):
    queryset = City.objects.all()
    serializer_class = CitySerializer