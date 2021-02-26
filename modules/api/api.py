#!/usr/bin/env python
# -*- coding: utf-8 -*

import json

import requests

import myclass.Weather as Weather
import myclass.Weather_circle as Circle
import myclass.Weather_forecast as Forecast
from gtts import gTTS
from playsound import playsound


# Permet d'obtenir les donnée d'une ville
def currentCity(city, key):
    # requete post
    url = "https://api.openweathermap.org/data/2.5/weather?q=%s&appid=%s&lang=fr&units=metric" % (city, key)
    x = requests.get(url)
    # Recup coordonnées
    result = Weather.weather_from_dict(json.loads(x.text))
    return result  # Permet d'obtenir les donnée d'une ville


def oneCity(city, key):
    # requete post
    url = "https://api.openweathermap.org/data/2.5/weather?q=%s&appid=%s&lang=fr&units=metric" % (city, key)
    x = requests.get(url)
    # Recup coordonnées
    result = Weather.weather_from_dict(json.loads(x.text))
    return result

def oneCitySpeak(city, key):
    # requete post
    url = "https://api.openweathermap.org/data/2.5/weather?q=%s&appid=%s&lang=fr&units=metric" % (city, key)
    x = requests.get(url)
    # Recup coordonnées
    result = Weather.weather_from_dict(json.loads(x.text))
    text = "Bulletin Météo pour %s" % result.name + ":""\t- Température actuel : " + str(
        round(result.main.temp)) + "°\t- Température minimal prévu : " + str(
        round(result.main.temp_min)) + "°\t- Température Maximal prévu : " + str(
        round(result.main.temp_max)) + "°\t- Humidité prévu : " + str(round(result.main.humidity)) + "%\t- " + \
           result.weather[0].description
    print("Bulletin Météo pour %s" % result.name + ":")
    print("\t- Température actuel : " + str(round(result.main.temp)) + "°c")
    print("\t- Température minimal prévu : " + str(round(result.main.temp_min)) + "°c")
    print("\t- Température Maximal prévu : " + str(round(result.main.temp_max)) + "°c")
    print("\t- Humidité prévu : " + str(round(result.main.humidity)) + "%")
    print("\t- " + result.weather[0].description)
    var = gTTS(text=text, lang="fr")
    var.save("annonceMeteo\meteo.mp3")
    playsound("annonceMeteo\meteo.mp3")

# Permet d'obtenir toutes les villes d'un périmètre en cercle
def circle(coord, key, cnt):
    # requete post
    url = "https://api.openweathermap.org/data/2.5/find?lat=%s&lon=%s&cnt=%s&appid=%s&lang=fr&units=metric" % (
        coord.lat, coord.lon, cnt, key)
    x = requests.get(url)
    # Recup coordonnées
    result = Circle.weather_circle_from_dict(json.loads(x.text))
    return result


# Permet d'obtenir toutes les données sur un forecast de 5 jours avec 3 Heures d'intervalle
def forecast(multi_city, key):
    tabCity = []
    # requete post
    for city in multi_city:
        url = "https://api.openweathermap.org/data/2.5/forecast?lang=fr&units=metric&q=%s&appid=%s" % (city.name, key)
        x = requests.get(url)
        result = Forecast.WeatherForecastfromdict(json.loads(x.text))
        tabCity.append(result)
    return tabCity
