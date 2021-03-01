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
mydb = mysql.connector.connect(host=hote, user=login, password=passw, database=db)
mycursor = mydb.cursor()


# creer la table du prof
def createTable():
    try:
        mycursor.execute('''CREATE TABLE aled (
                                town text,longitude int,
                                latitude int ,
                                date text,
                                temp int ,
                                temp_min int ,
                                temp_max int ,
                                humidity int ,
                                description text  )''')

        mydb.commit()
    except:
        print("La table existe déja")


# update ou insert into bdd forecast
def forecast(multiForecast_city):
    for i in multiForecast_city:
        for x in i.list:
            mycursor = mydb.cursor(buffered=True)
            # select une ville avec le temps et le nom de la ville
            sql = "SELECT id FROM aled WHERE town = %s and date= %s "
            adr = (i.city.name, x.dttxt)
            mycursor.execute(sql, adr)
            myresult = mycursor.fetchone()
            # if 0 isn't here if 1 isHere
            if mycursor.rowcount == 0:
                # insert la nouvelle donnée
                print("insert")
                sql = "INSERT INTO aled (town,longitude,latitude,date,temp,temp_min,temp_max,humidity,description) " \
                      "VALUES (%s, %s,%s, %s,%s, %s,%s, %s,%s) "
                val = (
                    i.city.name, i.city.coord.lon, i.city.coord.lat, x.dttxt, round(x.main.temp), round(x.main.tempmin),
                    round(x.main.tempmax), x.main.humidity, x.weather[0].description)
                mycursor.execute(sql, val)
                mydb.commit()
            else:
                # Update la donnée
                print("update")
                sql = "UPDATE aled SET temp= %s , temp_min = %s,temp_max= %s,humidity= %s ,description= %s " \
                      " where id = %s "
                val = (round(x.main.temp), round(x.main.tempmin), round(x.main.tempmax), x.main.humidity,
                       x.weather[0].description, myresult[0])
                mycursor.execute(sql, val)
                mydb.commit()
    print("sauvegarde en BBD fini")
