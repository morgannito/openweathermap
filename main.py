import json
import requests

# Latitude de Perpignan	42.6886591
# Longitude de Perpignan	2.8948332
attitude: float = 42.6886591
longitude: float = 2.8948332
api_key = "b8bdb7d52b20aa7c239f409d7f009840"


# todo refaire avec inpute longitute lattitude pui faire un forecast sur 5 jours pour toute les villes
# todo enregistre dans un csv avec 3 colonnes


def copie(tab):
    fichier = open("data.csv", "w+")
    fichier.write(tab)
    fichier.close()
    print("copie terminée")


def circle(att, long, key):
    cnt: int = 50
    # requete post
    url = "https://api.openweathermap.org/data/2.5/find?lat=%s&lon=%s&cnt=%s&appid=%s" % (
        att, long, cnt, key)
    x = requests.get(url)
    x = json.loads(x.text)
    x = x['list']
    i: int = 0
    tab = ""
    while i < cnt:
        y = x[i]
        main = y['main']
        # date = y['dt_txt']
        name = y['name']
        temp = main['temp'] - 273.15
        temp = round(temp)
        temp_min = main['temp_min'] - 273.15
        temp_min = round(temp_min)
        temp_max = main['temp_max'] - 273.15
        temp_max = round(temp_max)
        tab = tab + "Ville: %s \ntemperature : %s c\ntemperature min" \
                    " : %s c\ntemperature max : %s c\n" \
                    % (name, temp, temp_min, temp_max)
        i = i + 1
        copie(tab)


def meteo(city, key):
    # requete post
    url = "https://api.openweathermap.org/data/2.5/forecast?lang=fr&q=%s&appid=%s" % (city, key)
    x = requests.get(url)
    try:
        x = json.loads(x.text)
        x = x['list']
        print(x)
        i: int = 0
        tab = ""
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
            tab = tab + "Ville: %s  \ntemperature : %s c\ntemperature min" \
                        " : %s c\ntemperature max : %s c\ndate : %s \n" \
                        % (city, temp, temp_min, temp_max, date)
            i = i + 1
        copie(tab)
    except Exception as e:
        print(e)
        newCity = input('entre une nouvelle ville avec le bon nom cette fois ... \n')
        meteo(newCity, key)


# firstCity = input("Entrez la ville ")
# meteo(firstCity,api_key)
circle(attitude, longitude, api_key)
