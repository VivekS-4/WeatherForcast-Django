from django.urls import path
from . import views 
#New page URL would be added here

urlpatterns = [
    path('', views.Weather, name = "Weather"),
    path('Home', views.Home, name = "Homie"),
    path('About', views.About, name = "About"),
    path('Weather', views.Weather, name = "Weather"),
    path('admin', views.Login, name = "Login")
]