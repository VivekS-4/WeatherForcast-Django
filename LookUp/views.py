from django.shortcuts import render

def Home(request):
	#http://dataservice.accuweather.com/locations/v1/{LocationKey}
	import json
	import requests

	Weather_request = requests.get('https://api.openweathermap.org/data/2.5/weather?q=Delhi, IN&APPID=9636be5ebf7c35a32203f1be39b63934')

	try:
		api = json.loads(Weather_request.content)
	except Exception as e :
		api = "Error..."

	#return render(request, 'Home.html', {'air': air})
	return render(request, 'Home.html', {'api': api})

def About(request):
	return render(request, 'About.html', {})

def Weather(request):
	return render(request, 'Weather.html', {})

def Login(request):
	return render(request, 'admin', {})