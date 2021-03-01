import json

from fastapi import FastAPI
#!/usr/bin/env python
# -*- coding: utf-8 -*
import configparser  # Permet de parser le fichier de paramètres
import mysql.connector

config = configparser.RawConfigParser()  # On créé un nouvel objet "config"
config.read('./config.ini')  # On lit le fichier de paramètres
hote = config.get('DataBase', 'host')
login = config.get('DataBase', 'user')
passw = config.get('DataBase', 'pass')
db = config.get('DataBase', 'db')
mydb  = mysql.connector.connect(host=hote, user=login, password=passw, database=db)
mycursor = mydb .cursor()
app = FastAPI()

@app.get("/")
async def root():
    mycursor = mydb.cursor(buffered=True)
    mycursor.execute("SELECT * FROM aled WHERE town = 'Perpignan'")
    myresult = mycursor.fetchall()
    tab = []
    for i in myresult:
        ville = {"id": i[0], "city": i[1], "longitutde":i[2], "latitude": i[3], "time": i[4],
                 "temp": i[5],"min":i[6],"max":i[7],"humidity":i[8],"description":i[9]}
        tab.append(ville)

    return tab

