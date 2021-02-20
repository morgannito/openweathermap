import requests
import json
import modules.myVar as Var
import myclass.Weather as Weather
import myclass.Weather_circle as Circle
import myclass.Weather_forecast as Forecast


# Permet d'obtenir les donnée d'une ville
def currentCity(city, key):
    # requete post
    url = "https://api.openweathermap.org/data/2.5/weather?q=%s&appid=%s" % (city, key)
    x = requests.get(url)
    # Recup coordonnées
    result = Weather.weather_from_dict(json.loads(x.text))
    return result


# Permet d'obtenir toutes les villes d'un périmètre en cercle
def circle(coord, key, cnt):
    # requete post
    url = "https://api.openweathermap.org/data/2.5/find?lat=%s&lon=%s&cnt=%s&appid=%s" % (
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
        url = "https://api.openweathermap.org/data/2.5/forecast?lang=fr&q=%s&appid=%s" % (city.name, key)
        x = requests.get(url)
        result = Forecast.WeatherForecastfromdict(json.loads(x.text))
        tabCity.append(result)
    return tabCity

