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
                                description text  )''');

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
            adr = (i.city.name,x.dttxt)
            mycursor.execute(sql, adr)
            myresult = mycursor.fetchone()
            # if 0 isn't here if 1 isHere
            if mycursor.rowcount == 0 :
                # insert la nouvelle donnée
                print("insert")
                sql = "INSERT INTO aled (town,longitude,latitude,date,temp,temp_min,temp_max,humidity,description) VALUES (%s, %s,%s, %s,%s, %s,%s, %s,%s)"
                val = (i.city.name,i.city.coord.lon,i.city.coord.lat,x.dttxt,round(x.main.temp),round(x.main.tempmin),round(x.main.tempmax),x.main.humidity,x.weather[0].description)
                mycursor.execute(sql, val)
                mydb.commit()
            else:
                # Update la donnée
                print("update")
                sql = "UPDATE aled SET temp= %s , temp_min = %s,temp_max= %s,humidity= %s ,description= %s where id = %s  "
                val = (round(x.main.temp),round(x.main.tempmin),round(x.main.tempmax),x.main.humidity,x.weather[0].description,myresult[0])
                mycursor.execute(sql, val)
                mydb.commit()


# insert perso
def InsertWeather(weather):
    sql = "INSERT INTO coord (lon,lat) VALUES (%s, %s)"
    val = (weather.coord.lon,weather.coord.lat)
    mycursor.execute(sql, val)
    print("coord"+str(mycursor.lastrowid))
    id_coord = mycursor.lastrowid

    sql = "INSERT INTO main (temp,feels_like,temp_min,temp_max,pressure,humidity) VALUES (%s, %s,%s, %s,%s,%s)"
    val = (weather.main.temp, weather.main.feels_like, weather.main.temp_min, weather.main.temp_max, weather.main.pressure, weather.main.humidity)
    mycursor.execute(sql, val)
    print("main"+str(mycursor.lastrowid))
    id_main = mycursor.lastrowid

    sql = "INSERT INTO wind (speed,deg) VALUES (%s, %s)"
    val = (weather.wind.speed,weather.wind.deg)
    mycursor.execute(sql,val)
    print("wind"+str(mycursor.lastrowid))
    id_wind = mycursor.lastrowid

    query = "INSERT INTO clouds (alls) VALUES (%s)"
    mycursor.execute(query, (weather.clouds.all,))
    print("clouds"+str(mycursor.lastrowid))
    id_clouds = mycursor.lastrowid

    query = "INSERT IGNORE INTO sys (id,type,country,sunrise,sunset) VALUES (%s,%s,%s,%s,%s)"
    mycursor.execute(query, (weather.sys.id,weather.sys.type,weather.sys.country,weather.sys.sunrise,weather.sys.sunset,))
    print("sys"+str(mycursor.lastrowid))
    id_sys = mycursor.lastrowid

    query = "INSERT IGNORE INTO weatherElement (id,main,description,icon) VALUES (%s,%s,%s,%s)"
    mycursor.execute(query, (weather.weather[0].id,weather.weather[0].main,weather.weather[0].description,weather.weather[0].icon,))
    print("weatherElement"+str(mycursor.lastrowid))
    id_weather = weather.weather[0].id

    sql = "INSERT IGNORE INTO weather (id,id_coord,id_weatherElement,base,id_main,visibility,id_wind,id_clouds,dt,id_sys,timezone,name,cod) VALUES (%s, %s,%s, %s,%s,%s,%s, %s,%s, %s,%s,%s,%s)"
    val = (weather.id,id_coord,id_weather,weather.base,id_main,weather.visibility,id_wind,id_clouds,weather.dt,id_sys,weather.timezone,weather.name,weather.cod)
    mycursor.execute(sql, val)
    print("weather"+str(mycursor.lastrowid))

    mydb.commit()
    return True



def verif(weather):
    mycursor = mydb.cursor(buffered=True)
    sql = "SELECT * FROM weather WHERE id = %s"
    adr = (weather.id,)
    mycursor.execute(sql, adr)
    # if 0 isn't here if 1 isHere
    return mycursor.rowcount



