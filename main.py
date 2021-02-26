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

# Just For Fun
print(colored(text2art("OpenWeather"),'cyan'))
print(colored('Created by Morgannito \n\n'.center(60), 'red'))

# Recup la clé API du Fichier config.ini
api_key = config.get('API', 'api_key')
cnt: int = 10

# firstCity = input("Entrez la ville ")
firstCity = "Perpignan"
test = api.oneCity(firstCity, api_key)
#sql.createTable()
#sql.InsertWeather(test)
#sql.verif(test)

#
City = api.currentCity(firstCity, api_key)
multiCity = api.circle(City.coord, api_key, cnt)
multiForecast_city = api.forecast(multiCity.list, api_key)
sql.forecast(multiForecast_city)
# csv.copie(multiForecast_city)
# csv.recherche(firstCity)
#
