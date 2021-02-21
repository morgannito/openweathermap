#!/usr/bin/env python
# -*-coding: utf-8 -*

import modules.api.api as api
import modules.csv.csv as csv
import configparser  # Permet de parser le fichier de paramètres

config = configparser.RawConfigParser()  # On créé un nouvel objet "config"
config.read('config.ini')  # On lit le fichier de paramètres
api_key = config.get('API', 'api_key')
cnt: int = 10

# firstCity = input("Entrez la ville ")
firstCity = "Perpignan"
api.oneCity(firstCity, api_key)


City = api.currentCity(firstCity, api_key)
multiCity = api.circle(City.coord, api_key, cnt)
multiForecast_city = api.forecast(multiCity.list, api_key)
csv.copie(multiForecast_city)
csv.recherche(firstCity)

