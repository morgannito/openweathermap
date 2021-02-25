#!/usr/bin/python3
import json
from dataclasses import dataclass
from typing import Any, List, TypeVar, Callable, Type, cast

import requests
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, Text
from sqlalchemy.orm import sessionmaker, relationship, mapper
from sqlalchemy.ext.declarative import declarative_base
T = TypeVar("T")

# Base class used by my classes (my entities)
Base = declarative_base()  # Required





def from_float(x):
    assert isinstance(x, (float, int)) and not isinstance(x, bool)
    return float(x)


def to_float(x):
    assert isinstance(x, float)
    return x


def from_str(x):
    assert isinstance(x, str)
    return x


def from_list(f, x):
    assert isinstance(x, list)
    return [f(y) for y in x]


def to_class(c, x):
    assert isinstance(x, c)
    return x.to_dict()


class Clouds(Base):
    __tablename__ = 'clouds'
    id = Column(Integer, primary_key=True, autoincrement=True)
    all = Column(Integer)

    def __init__(self, all):
        self.all = all

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        all = obj.get("all")
        return Clouds(all)

    def to_dict(self):
        result = {}
        result["all"] = self.all
        return result


class Coord(Base):
    __tablename__ = 'coord'
    id = Column(Integer, primary_key=True,autoincrement=True)
    lon = Column(Integer)
    lat = Column(Integer)

    def __init__(self, lon, lat):
        self.lon = lon
        self.lat = lat

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        lon = from_float(obj.get("lon"))
        lat = from_float(obj.get("lat"))
        return Coord(lon, lat)

    def to_dict(self):
        result = {}
        result["lon"] = to_float(self.lon)
        result["lat"] = to_float(self.lat)
        return result


class Main(Base):
    __tablename__ = 'main'
    id = Column(Integer, primary_key=True)
    temp = Column(Text)
    feelslike = Column(Text)
    tempmin = Column(Text)
    tempmax = Column(Text)
    pressure = Column(Text)
    humidity = Column(Text)

    def __init__(self, temp, feelslike, tempmin, tempmax, pressure, humidity):
        self.temp = temp
        self.feelslike = feelslike
        self.tempmin = tempmin
        self.tempmax = tempmax
        self.pressure = pressure
        self.humidity = humidity

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        temp = obj.get("temp")
        feelslike = obj.get("feels_like")
        tempmin = obj.get("temp_min")
        tempmax = obj.get("temp_max")
        pressure = obj.get("pressure")
        humidity = obj.get("humidity")
        return Main(temp, feelslike, tempmin, tempmax, pressure, humidity)

    def to_dict(self):
        result = {}
        result["temp"] = to_float(self.temp)
        result["feels_like"] = to_float(self.feelslike)
        result["temp_min"] = self.tempmin
        result["temp_max"] = self.tempmax
        result["pressure"] = self.pressure
        result["humidity"] = self.humidity
        return result


class Sys(Base):
    __tablename__ = 'sys'
    id = Column(Integer, primary_key=True)
    type = Column(Integer)
    country = Column(Text)
    sunrise = Column(Integer)
    sunset = Column(Integer)


    def __init__(self, type, id, country, sunrise, sunset):
        self.type = type
        self.id = id
        self.country = country
        self.sunrise = sunrise
        self.sunset = sunset

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        type = obj.get("type")
        id = obj.get("id")
        country = from_str(obj.get("country"))
        sunrise = obj.get("sunrise")
        sunset = obj.get("sunset")
        return Sys(type, id, country, sunrise, sunset)

    def to_dict(self):
        result = {}
        result["type"] = self.type
        result["id"] = self.id
        result["country"] = from_str(self.country)
        result["sunrise"] = self.sunrise
        result["sunset"] = self.sunset
        return result


class WeatherElement(Base):
    __tablename__ = 'weatherElement'
    id = Column(Integer, primary_key=True)
    main = Column(Text)
    description = Column(Text)
    icon = Column(Text)

    def __init__(self, id, main, description, icon):
        self.id = id
        self.main = main
        self.description = description
        self.icon = icon

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        id = obj.get("id")
        main = from_str(obj.get("main"))
        description = from_str(obj.get("description"))
        icon = from_str(obj.get("icon"))
        return WeatherElement(id, main, description, icon)

    def to_dict(self):
        result = {}
        result["id"] = self.id
        result["main"] = from_str(self.main)
        result["description"] = from_str(self.description)
        result["icon"] = from_str(self.icon)
        return result


class Wind(Base):
    __tablename__ = 'wind'
    id = Column(Integer, primary_key=True, autoincrement=True)
    speed = Column(Integer)
    deg = Column(Integer)

    def __init__(self, speed, deg):
        self.speed = speed
        self.deg = deg

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        speed = obj.get("speed")
        deg = obj.get("deg")
        return Wind(speed, deg)

    def to_dict(self):
        result = {}
        result["speed"] = to_float(self.speed)
        result["deg"] = self.deg
        return result


class Weather(Base):
    __tablename__ = 'weather'

    id = Column(Integer, primary_key=True)

    id_coord = Column(Integer, ForeignKey("coord.id"))
    coord = relationship("Coord", foreign_keys=[id_coord])


    #id_weather = Column(Integer, ForeignKey("weatherElement.id"))
    #weather = relationship("WeatherElement", foreign_keys=[id_weather])

    base = Column(Text)

    id_main = Column(Integer, ForeignKey("main.id"))
    main = relationship("Main", foreign_keys=[id_main])

    visibility = Column(Integer) # int

    id_wind = Column(Integer, ForeignKey("wind.id"))
    wind = relationship("Wind", foreign_keys=[id_wind])

    id_clouds = Column(Integer, ForeignKey("clouds.id"))
    clouds = relationship("Clouds", foreign_keys=[id_clouds])


    dt = Column(Integer)# date

    id_sys = Column(Integer, ForeignKey("sys.id"))
    sys = relationship("Sys", foreign_keys=[id_sys])

    timezone = Column(Integer)
    name = Column(Text)
    cod = Column(Integer)

    def __init__(self, coord, weather, base, main, visibility, wind, clouds, dt, sys, timezone, id, name, cod):
        self.coord = coord
        self.weather = weather
        self.base = base
        self.main = main
        self.visibility = visibility
        self.wind = wind
        self.clouds = clouds
        self.dt = dt
        self.sys = sys
        self.timezone = timezone
        self.id = id
        self.name = name
        self.cod = cod

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        coord = Coord.from_dict(obj.get("coord"))
        weather = from_list(WeatherElement.from_dict, obj.get("weather"))
        base = from_str(obj.get("base"))
        main = Main.from_dict(obj.get("main"))
        visibility = obj.get("visibility")
        wind = Wind.from_dict(obj.get("wind"))
        clouds = Clouds.from_dict(obj.get("clouds"))
        dt = obj.get("dt")
        sys = Sys.from_dict(obj.get("sys"))
        timezone = obj.get("timezone")
        id = obj.get("id")
        name = from_str(obj.get("name"))
        cod = obj.get("cod")
        return Weather(coord, weather, base, main, visibility, wind, clouds, dt, sys, timezone, id, name, cod)

    def to_dict(self):
        result = {}
        result["coord"] = to_class(Coord, self.coord)
        result["weather"] = from_list(lambda x: to_class(WeatherElement, x), self.weather)
        result["base"] = from_str(self.base)
        result["main"] = to_class(Main, self.main)
        result["visibility"] = self.visibility
        result["wind"] = to_class(Wind, self.wind)
        result["clouds"] = to_class(Clouds, self.clouds)
        result["dt"] = self.dt
        result["sys"] = to_class(Sys, self.sys)
        result["timezone"] = self.timezone
        result["id"] = self.id
        result["name"] = from_str(self.name)
        result["cod"] = self.cod
        return result


def Weatherfromdict(s):
    return Weather.from_dict(s)

# The main part
if __name__ == '__main__':

    # engine = create_engine('sqlite:///demo.db', echo=False)
    engine = create_engine("mysql://user:mdp@82.65.123.20/weather", pool_size=10, max_overflow=20)

    print("--- Construct all tables for the database (here just one table) ---")
    Base.metadata.create_all(engine)  # Only for the first time

    print("--- Create three new contacts and push its into the database ---")
    Session = sessionmaker(bind=engine)
    session = Session()

    url = "https://api.openweathermap.org/data/2.5/weather?q=%s&appid=%s&lang=fr&units=metric" % ("Perpignan", "b8bdb7d52b20aa7c239f409d7f009840")
    x = requests.get(url)
    # Recup coordonnées
    print(x.text)
    result = Weatherfromdict(json.loads(x.text))
    session.add(result)

    session.commit()