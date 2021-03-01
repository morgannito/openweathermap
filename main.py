#!/usr/bin/env python
# -*-coding: utf-8 -*

import modules.api.api as api
import modules.csv.csv as csv
import configparser  # Permet de parser le fichier de paramètres
import modules.sql.sql as sql
from art import *
from termcolor import colored

config = configparser.RawConfigParser()  # On créé un nouvel objet "config"
config.read('config.ini')  # On lit le fichier de paramètres
# # Recup la clé API du Fichier config.ini
api_key = config.get('API', 'api_key')
cnt: int = 50


# Just For Fun
print(colored(text2art("OpenWeather"),'cyan'))
print(colored('Created by Morgannito \n\n'.center(60), 'red'))

# firstCity = input("Entrez la ville ")
firstCity = "Perpignan"

# Requete avec l'api
City = api.currentCity(firstCity, api_key)
multiCity = api.circle(City.coord, api_key, cnt)
multiForecast_city = api.forecast(multiCity.list, api_key)

# Enregistrement des données
csv.copie(multiForecast_city)
csv.recherche(firstCity)

sql.forecast(multiForecast_city)
