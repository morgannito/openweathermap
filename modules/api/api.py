import requests
import json
import modules.myVar as Var


# Permet d'obtenir les coordonnées d'une ville
def currentCoord(city, key):
    # requete post
    url = "https://api.openweathermap.org/data/2.5/weather?q=%s&appid=%s" % (city, key)
    x = requests.get(url)
    x = json.loads(x.text)
    # Recup coordonnée
    x = x['coord']
    lat = x['lat']
    lon = x['lon']
    coord = [lat, lon]
    return coord


# Permet d'obtenir toutes d'un périmètre en cercle
def circle(att, long, key, cnt):
    # requete post
    url = "https://api.openweathermap.org/data/2.5/find?lat=%s&lon=%s&cnt=%s&appid=%s" % (
        att, long, cnt, key)
    x = requests.get(url)
    x = json.loads(x.text)
    x = x['list']
    i: int = 0
    circleCity = []
    while i < cnt:
        y = x[i]
        print(y['name'])
        circleCity.append(y['name'])
        i = i + 1
    return circleCity


# Permet d'obtenir toutes les données sur un forecast de 5 jours avec 3 Heures d'intervalle
def forecast(city, key):
    # requete post
    url = "https://api.openweathermap.org/data/2.5/forecast?lang=fr&q=%s&appid=%s" % (city, key)
    x = requests.get(url)
    try:
        x = json.loads(x.text)
        x = x['list']
        i: int = 0
        while i < 40:
            y = x[i]
            main = y['main']
            date = y['dt_txt']
            temp = main['temp'] - 273.15
            temp = round(temp)
            temp_min = main['temp_min'] - 273.15
            temp_min = round(temp_min)
            temp_max = main['temp_max'] - 273.15
            temp_max = round(temp_max)
            Var.tabCity = Var.tabCity + "Ville: %s  \ntemperature : %s c\ntemperature min" \
                                        " : %s c\ntemperature max : %s c\ndate : %s \n" \
                                        % (city, temp, temp_min, temp_max, date)
            i = i + 1
    except Exception as e:
        print(e)
        newCity = input('entre une nouvelle ville avec le bon nom cette fois ... \n')
        forecast(newCity, key)
    return Var.tabCity
