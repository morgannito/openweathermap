#!/usr/bin/env python
# -*- coding: utf-8 -*
import configparser  # Permet de parser le fichier de paramètres
import mysql.connector

config = configparser.RawConfigParser()  # On créé un nouvel objet "config"
config.read('./../../config.ini')  # On lit le fichier de paramètres
hote = config.get('MYSQL', 'host')
login = config.get('MYSQL', 'user')
passw = config.get('MYSQL', 'pass')
db = config.get('MYSQL', 'db')

# coding: utf-8


conn = mysql.connector.connect(host=hote, user=login, password=passw, database=db)
cursor = conn.cursor()
conn.close()
