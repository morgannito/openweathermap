#!/usr/bin/env python
# -*- coding: utf-8 -*


import json
import requests
from dataclasses import dataclass
from typing import Any, List, TypeVar, Callable, Type, cast
from sqlalchemy import Column, Integer, ForeignKey, Text
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

Base = declarative_base()  # Required
T = TypeVar("T")


def from_int(x: Any) -> int:
    assert isinstance(x, int) and not isinstance(x, bool)
    return x


def from_float(x: Any) -> float:
    assert isinstance(x, (float, int)) and not isinstance(x, bool)
    return float(x)


def to_float(x: Any) -> float:
    assert isinstance(x, float)
    return x


def from_str(x: Any) -> str:
    assert isinstance(x, str)
    return x


def from_list(f: Callable[[Any], T], x: Any) -> List[T]:
    assert isinstance(x, list)
    return [f(y) for y in x]


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


@dataclass
class Clouds(Base):

    all: int

    __tablename__ = 'clouds'
    id = Column(Integer, primary_key=True, autoincrement=True)
    all = Column(Integer)

    def __init__(self, all):
        self.all = all

    @staticmethod
    def from_dict(obj: Any) -> 'Clouds':
        assert isinstance(obj, dict)
        all = from_int(obj.get("all"))
        return Clouds(all)

    def to_dict(self) -> dict:
        result: dict = {}
        result["all"] = from_int(self.all)
        return result


@dataclass
class Coord(Base):
    lon: float
    lat: float

    __tablename__ = 'coord'
    id = Column(Integer, primary_key=True, autoincrement=True)
    lon = Column(Integer)
    lat = Column(Integer)

    def __init__(self, lon, lat):
        self.lon = lon
        self.lat = lat

    @staticmethod
    def from_dict(obj: Any) -> 'Coord':
        assert isinstance(obj, dict)
        lon = from_float(obj.get("lon"))
        lat = from_float(obj.get("lat"))
        return Coord(lon, lat)

    def to_dict(self) -> dict:
        result: dict = {}
        result["lon"] = to_float(self.lon)
        result["lat"] = to_float(self.lat)
        return result


@dataclass
class Main(Base):
    temp: float
    feels_like: float
    temp_min: float
    temp_max: float
    pressure: int
    humidity: int

    __tablename__ = 'main'
    id = Column(Integer, primary_key=True)
    temp = Column(Text)
    feels_like = Column(Text)
    temp_min = Column(Text)
    temp_max = Column(Text)
    pressure = Column(Text)
    humidity = Column(Text)

    def __init__(self, temp, feels_like, temp_min, temp_max, pressure, humidity):
        self.temp = temp
        self.feels_like = feels_like
        self.temp_min = temp_min
        self.temp_max = temp_max
        self.pressure = pressure
        self.humidity = humidity

    @staticmethod
    def from_dict(obj: Any) -> 'Main':
        assert isinstance(obj, dict)
        temp = from_float(obj.get("temp"))
        feels_like = from_float(obj.get("feels_like"))
        temp_min = from_float(obj.get("temp_min"))
        temp_max = from_float(obj.get("temp_max"))
        pressure = from_int(obj.get("pressure"))
        humidity = from_int(obj.get("humidity"))
        return Main(temp, feels_like, temp_min, temp_max, pressure, humidity)

    def to_dict(self) -> dict:
        result: dict = {}
        result["temp"] = to_float(self.temp)
        result["feels_like"] = to_float(self.feels_like)
        result["temp_min"] = to_float(self.temp_min)
        result["temp_max"] = to_float(self.temp_max)
        result["pressure"] = from_int(self.pressure)
        result["humidity"] = from_int(self.humidity)
        return result


@dataclass
class Sys(Base):
    type: int
    id: int
    country: str
    sunrise: int
    sunset: int

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
    def from_dict(obj: Any) -> 'Sys':
        assert isinstance(obj, dict)
        type = from_int(obj.get("type"))
        id = from_int(obj.get("id"))
        country = from_str(obj.get("country"))
        sunrise = from_int(obj.get("sunrise"))
        sunset = from_int(obj.get("sunset"))
        return Sys(type, id, country, sunrise, sunset)

    def to_dict(self) -> dict:
        result: dict = {}
        result["type"] = from_int(self.type)
        result["id"] = from_int(self.id)
        result["country"] = from_str(self.country)
        result["sunrise"] = from_int(self.sunrise)
        result["sunset"] = from_int(self.sunset)
        return result


@dataclass
class WeatherElement:
    id: int
    main: str
    description: str
    icon: str

    @staticmethod
    def from_dict(obj: Any) -> 'WeatherElement':
        assert isinstance(obj, dict)
        id = from_int(obj.get("id"))
        main = from_str(obj.get("main"))
        description = from_str(obj.get("description"))
        icon = from_str(obj.get("icon"))
        return WeatherElement(id, main, description, icon)

    def to_dict(self) -> dict:
        result: dict = {}
        result["id"] = from_int(self.id)
        result["main"] = from_str(self.main)
        result["description"] = from_str(self.description)
        result["icon"] = from_str(self.icon)
        return result


@dataclass
class Wind(Base):
    speed: float
    deg: int


    __tablename__ = 'wind'
    id = Column(Integer, primary_key=True, autoincrement=True)
    speed = Column(Integer)
    deg = Column(Integer)

    def __init__(self, speed, deg):
        self.speed = speed
        self.deg = deg
    @staticmethod
    def from_dict(obj: Any) -> 'Wind':
        assert isinstance(obj, dict)
        speed = from_float(obj.get("speed"))
        deg = from_int(obj.get("deg"))
        return Wind(speed, deg)

    def to_dict(self) -> dict:
        result: dict = {}
        result["speed"] = to_float(self.speed)
        result["deg"] = from_int(self.deg)
        return result


@dataclass
class Weather(Base):
    coord: Coord
    weather: List[WeatherElement]
    base: str
    main: Main
    visibility: int
    wind: Wind
    clouds: Clouds
    dt: int
    sys: Sys
    timezone: int
    id: int
    name: str
    cod: int

    __tablename__ = 'weather'

    id = Column(Integer, primary_key=True)

    id_coord = Column(Integer, ForeignKey("coord.id"))
    coord = relationship("Coord", foreign_keys=[id_coord])


    weather = Column(Text)

    # id_weather = Column(Integer, ForeignKey("weatherElement.id"))
    # weather = relationship("WeatherElement", foreign_keys=[id_weather])

    base = Column(Text)

    id_main = Column(Integer, ForeignKey("main.id"))
    main = relationship("Main", foreign_keys=[id_main])

    visibility = Column(Integer)  # int

    id_wind = Column(Integer, ForeignKey("wind.id"))
    wind = relationship("Wind", foreign_keys=[id_wind])

    id_clouds = Column(Integer, ForeignKey("clouds.id"))
    clouds = relationship("Clouds", foreign_keys=[id_clouds])

    dt = Column(Integer)  # date

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
    def from_dict(obj: Any) -> 'Weather':
        assert isinstance(obj, dict)
        coord = Coord.from_dict(obj.get("coord"))
        weather = from_list(WeatherElement.from_dict, obj.get("weather"))
        base = from_str(obj.get("base"))
        main = Main.from_dict(obj.get("main"))
        visibility = from_int(obj.get("visibility"))
        wind = Wind.from_dict(obj.get("wind"))
        clouds = Clouds.from_dict(obj.get("clouds"))
        dt = from_int(obj.get("dt"))
        sys = Sys.from_dict(obj.get("sys"))
        timezone = from_int(obj.get("timezone"))
        id = from_int(obj.get("id"))
        name = from_str(obj.get("name"))
        cod = from_int(obj.get("cod"))
        return Weather(coord, weather, base, main, visibility, wind, clouds, dt, sys, timezone, id, name, cod)

    def to_dict(self) -> dict:
        result: dict = {}
        result["coord"] = to_class(Coord, self.coord)
        result["weather"] = from_list(lambda x: to_class(WeatherElement, x), self.weather)
        result["base"] = from_str(self.base)
        result["main"] = to_class(Main, self.main)
        result["visibility"] = from_int(self.visibility)
        result["wind"] = to_class(Wind, self.wind)
        result["clouds"] = to_class(Clouds, self.clouds)
        result["dt"] = from_int(self.dt)
        result["sys"] = to_class(Sys, self.sys)
        result["timezone"] = from_int(self.timezone)
        result["id"] = from_int(self.id)
        result["name"] = from_str(self.name)
        result["cod"] = from_int(self.cod)
        return result


def weather_from_dict(s: Any) -> Weather:
    return Weather.from_dict(s)


def weather_to_dict(x: Weather) -> Any:
    return to_class(Weather, x)


# The main part
if __name__ == '__main__':

    # engine = create_engine('sqlite:///demo.db', echo=False)
    engine = create_engine("mysql://weather:weather@82.65.123.20/weather", pool_size=10, max_overflow=20)

    print("--- Construct all tables for the database ---")
    Base.metadata.create_all(engine)  # Only for the first time

    print("--- Create three new contacts and push its into the database ---")
    Session = sessionmaker(bind=engine)
    session = Session()
    url = "https://api.openweathermap.org/data/2.5/weather?q=%s&appid=%s&lang=fr&units=metric" % ("Paris", "b8bdb7d52b20aa7c239f409d7f009840")
    x = requests.get(url)
    # Recup coordonnées
    print(x.text)
    result = weather_from_dict(json.loads(x.text))
    session.add(result)

    session.commit()