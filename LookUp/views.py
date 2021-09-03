from django.shortcuts import render
import requests
from .models import City
from .forms import CityForm
import json
url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=9636be5ebf7c35a32203f1be39b63934'
lat = str(28.37169)
lg = str(77.056508)
cc = "IN" #Country Code, Whenever going to user zipcode of another country change this here to that COUNTRY CODE

def index(request):
    form = CityForm()
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
    return render(request, 'index.html', {'weather_data' : weather_data, 'form': form}) #returns the index.html template



def Search(request):
    if request.method == "POST":
        zipcode = request.POST.get("zipcode", False)
        Weather_request = requests.get('http://api.openweathermap.org/data/2.5/weather?zip='+ zipcode +','+ cc +'&units=imperial&appid=b4baae3fd8dfcb64b615a38104ae65bc').json()
        # requests.get('http://api.openweathermap.org/data/2.5/weather?q=New%20Delhi&units=imperial&appid=9636be5ebf7c35a32203f1be39b63934')
        air_request = requests.get('https://api.weatherbit.io/v2.0/current/airquality?&postal_code='+ zipcode +'&key=7821ab051eb04daaa20e2c2fd19caec9') #valid till 02/10/21
        try:
            wth = (Weather_request)
            api = json.loads(air_request.content)
        except Exception as e :
            wth = "Weather Error...",
            api = "Air Quality Error"
        return render(request, 'Search.html', {'api': api, 'wth': wth, 'zipcode': zipcode}) 
    


def Home(request):
    return render(request, 'Home.html', {})

def About(request):
	return render(request, 'About.html', {})

def Login(request):
	return render(request, 'admin', {})
