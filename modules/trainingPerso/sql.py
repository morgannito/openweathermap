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
