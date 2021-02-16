import json
import requests
import csv


# Latitude de Perpignan	42.6886591
# Longitude de Perpignan	2.8948332

api_key = "b8bdb7d52b20aa7c239f409d7f009840"
global tabCity
tabCity = ""

global csvCity
csvCity = []

def recherche(villeRecherche):
    with open('Alentours de Toulouges.csv', newline='') as f:
        tableau = []
        lire = csv.reader(f)
        for ligne in lire:
            tableau.append(ligne)
            if ligne[0] == villeRecherche:
                if len(csvCity) < 40:
                   yolo = ligne[1].split(";")
                   dic = {"ville":ligne[0], "pays": yolo[0], "date": yolo[1],"temp":yolo[2],"min":yolo[3],"max":yolo[4]}
                   csvCity.append(dic)
    jsondata = json.dumps(csvCity).encode("utf8")
    copieJson(jsondata)

def copieJson(tab):
    fichier = open("json.json", "wb")
    fichier.write(tab)
    fichier.close()
    print("copie terminée")

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
    circleCity = []
    while i < cnt:
        y = x[i]
        print(y['name'])
        circleCity.append(y['name'])
        i = i + 1
    return circleCity


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
            global tabCity
            tabCity = tabCity + "Ville: %s  \ntemperature : %s c\ntemperature min" \
                                " : %s c\ntemperature max : %s c\ndate : %s \n" \
                                % (city, temp, temp_min, temp_max, date)
            i = i + 1
    except Exception as e:
        print(e)
        newCity = input('entre une nouvelle ville avec le bon nom cette fois ... \n')
        forecast(newCity, key)
    return tabCity


# firstCity = input("Entrez la ville ")
# coord = currentCoord(firstCity, api_key)
# multiCity = circle(coord[0], coord[1], api_key)

# for i in multiCity:
#    forecast(i, api_key)
# copie(tabCity)

recherche("Toulouges")