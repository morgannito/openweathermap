#!/usr/bin/env python
# -*-coding: utf-8 -*

import modules.api.api as api
import modules.csv.csv as csv
import modules.myVar as Var

#firstCity = input("Entrez la ville ")
firstCity = "Perpignan"

City = api.currentCity(firstCity, Var.api_key)
multiCity = api.circle(City.coord, Var.api_key, Var.cnt)
multiForecast_city = api.forecast(multiCity.list, Var.api_key)
csv.copie(multiForecast_city)

csv.recherche(firstCity)
