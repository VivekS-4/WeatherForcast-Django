from django.shortcuts import render
import requests
from .models import City
from .forms import CityForm
url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=9636be5ebf7c35a32203f1be39b63934'
import json

def index(request):

    form = CityForm()
    # city = 'Las Vegas'
    cities = City.objects.all()
    if request.method == 'POST': # only true if form is submitted
        form = CityForm(request.POST) # add actual request data to form for processing
        form.save() # will validate and save if validate

    weather_data = []


    for city in cities:

        city_weather = requests.get(url.format(city)).json() #request the API data and convert the JSON to Python data types
        weather = {
            'city' : city,
            'temperature' : city_weather['main']['temp'],
            'description' : city_weather['weather'][0]['description'],
            'icon' : city_weather['weather'][0]['icon']
        }
    weather_data.append(weather)
    context = {'weather_data' : weather_data, 'form': form}
    return render(request, 'index.html', context) #returns the index.html template



def Home(request):
	cities = City.objects.all() #return all the cities in the database
	if request.method == 'POST': # only true if form is submitted
		form = CityForm(request.POST) # add actual request data to form for processing
		form.save()

	form = CityForm()
	weather_data = []
	context = {'weather_data' : weather_data, 'form' : form}
	for city in cities:
		try:
			city_weather = requests.get(url.format(city)).json() #request the API data and convert the JSON to Python data types
			weather = {
            'city' : city,
            'temperature' : city_weather['main']['temp'],
            'description' : city_weather['weather'][0]['description'],
            'icon' : city_weather['weather'][0]['icon']
			}
		except Exception as e:
			city_weather = " Weather Error"
	
	weather_data.append(weather) #add the data for the current city into our list
	context = {'weather_data' : weather_data}
	return render(request, 'Home.html', context) #returns the index.html template


def Search(request):
	Weather_request = requests.get('https://api.openweathermap.org/data/2.5/weather?q=Delhi,IN&APPID=9636be5ebf7c35a32203f1be39b63934') 
	air_request = requests.get('https://www.airnowapi.org/aq/observation/latLong/current/?format=application/json&latitude=28.621763&longitude=77.055823&distance=25&API_KEY=5C93347A-7199-4983-9D49-73D9F0DD49C3')

	try:
		aqi = json.loads(Weather_request.content)
		api = json.loads(air_request.content)
	except Exception as e :
		aqi = "Weather Error...",
		api = "Air Quality Error"
	return render(request, 'Search.html', {'api': api, 'aqi': aqi})

def About(request):
	return render(request, 'About.html', {})

def Login(request):
	return render(request, 'admin', {})

