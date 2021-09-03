from django.urls import path, include
from . import views 
#New page URL would be added here

urlpatterns = [
    path('', views.Home, name = "Home"),
    path('Home', views.index, name = "index"),
    path('Results', views.Search, name = "Search"),
    path('About', views.About, name = "About"),
    path('./admin', views.Login, name = "Login"),
    path('accounts/', include('django.contrib.auth.urls')),
]
