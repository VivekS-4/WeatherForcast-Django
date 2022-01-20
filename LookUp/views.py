from django.shortcuts import render
import datetime
import requests
from .models import City
from .forms import CityForm
import json
url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=9636be5ebf7c35a32203f1be39b63934'
index_key = '8dd07bd89a83283a4c72e4ad17e1befc'
zipcode = '000000'
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
            'icon' : city_weather['weather'][0]['icon'],
            'description' : city_weather['weather'][0]['description']
        }
        weather_data.append(weather)
    return render(request, 'index.html', {'weather_data' : weather_data, 'form': form}) #returns the index.html template



def Search(request):
    if request.method == "POST":
        today = datetime.date.today()
        zipcode = request.POST.get("zipcode", False)
        Weather_request = requests.get('http://api.openweathermap.org/data/2.5/weather?zip='+ zipcode +','+ cc +'&units=imperial&appid=8dd07bd89a83283a4c72e4ad17e1befc').json()
        url = "https://api.ambeedata.com/latest/by-postal-code"
        querystring = {"postalCode":zipcode ,"countryCode":"IN"}
        headers = {
            'x-api-key': "7d1d11ece927ea42db9dd51c32ddd180a4bbb4d14feb94f99883bb8fcad32223",
            'Content-type': "application/json"
            }
        response = requests.request("GET", url, headers=headers, params=querystring).json()
        try:
            wth = (Weather_request)
            api = response
        except Exception as e :
            wth = "Weather Error..."
            api = "Air Quality Error"
        return render(request, 'Search.html', {'ap': api, 'wth': wth, 'zipcode': zipcode, 'td': today}) 

def Home(request):
    return render(request, 'Home.html', {})

def About(request):
	return render(request, 'About.html', {})

def Login(request):
	return render(request, 'admin', {})
