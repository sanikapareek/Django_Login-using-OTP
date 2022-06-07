from django.contrib import admin
from django.urls import path,include
from login import views



urlpatterns = [
    path('', views.load, name="load"), #name=login is name of the function in views.login( views of login app)
    path('login', views.login, name="login"),
    path('home', views.home, name="home")
]
