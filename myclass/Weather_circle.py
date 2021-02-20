from dataclasses import dataclass
from typing import Any, List, TypeVar, Callable, Type, cast


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


def from_none(x: Any) -> Any:
    assert x is None
    return x


def from_list(f: Callable[[Any], T], x: Any) -> List[T]:
    assert isinstance(x, list)
    return [f(y) for y in x]


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


@dataclass
class Clouds:
    all: int

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
class Coord:
    lat: float
    lon: float

    @staticmethod
    def from_dict(obj: Any) -> 'Coord':
        assert isinstance(obj, dict)
        lat = from_float(obj.get("lat"))
        lon = from_float(obj.get("lon"))
        return Coord(lat, lon)

    def to_dict(self) -> dict:
        result: dict = {}
        result["lat"] = to_float(self.lat)
        result["lon"] = to_float(self.lon)
        return result


@dataclass
class Main:
    temp: float
    feels_like: float
    temp_min: float
    temp_max: float
    pressure: int
    humidity: int

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
class Sys:
    country: str

    @staticmethod
    def from_dict(obj: Any) -> 'Sys':
        assert isinstance(obj, dict)
        country = from_str(obj.get("country"))
        return Sys(country)

    def to_dict(self) -> dict:
        result: dict = {}
        result["country"] = from_str(self.country)
        return result


@dataclass
class Weather:
    id: int
    main: str
    description: str
    icon: str

    @staticmethod
    def from_dict(obj: Any) -> 'Weather':
        assert isinstance(obj, dict)
        id = from_int(obj.get("id"))
        main = from_str(obj.get("main"))
        description = from_str(obj.get("description"))
        icon = from_str(obj.get("icon"))
        return Weather(id, main, description, icon)

    def to_dict(self) -> dict:
        result: dict = {}
        result["id"] = from_int(self.id)
        result["main"] = from_str(self.main)
        result["description"] = from_str(self.description)
        result["icon"] = from_str(self.icon)
        return result


@dataclass
class Wind:
    speed: float
    deg: int

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
class ListElement:
    id: int
    name: str
    coord: Coord
    main: Main
    dt: int
    wind: Wind
    sys: Sys
    rain: None
    snow: None
    clouds: Clouds
    weather: List[Weather]

    @staticmethod
    def from_dict(obj: Any) -> 'ListElement':
        assert isinstance(obj, dict)
        id = from_int(obj.get("id"))
        name = from_str(obj.get("name"))
        coord = Coord.from_dict(obj.get("coord"))
        main = Main.from_dict(obj.get("main"))
        dt = from_int(obj.get("dt"))
        wind = Wind.from_dict(obj.get("wind"))
        sys = Sys.from_dict(obj.get("sys"))
        rain = from_none(obj.get("rain"))
        snow = from_none(obj.get("snow"))
        clouds = Clouds.from_dict(obj.get("clouds"))
        weather = from_list(Weather.from_dict, obj.get("weather"))
        return ListElement(id, name, coord, main, dt, wind, sys, rain, snow, clouds, weather)

    def to_dict(self) -> dict:
        result: dict = {}
        result["id"] = from_int(self.id)
        result["name"] = from_str(self.name)
        result["coord"] = to_class(Coord, self.coord)
        result["main"] = to_class(Main, self.main)
        result["dt"] = from_int(self.dt)
        result["wind"] = to_class(Wind, self.wind)
        result["sys"] = to_class(Sys, self.sys)
        result["rain"] = from_none(self.rain)
        result["snow"] = from_none(self.snow)
        result["clouds"] = to_class(Clouds, self.clouds)
        result["weather"] = from_list(lambda x: to_class(Weather, x), self.weather)
        return result


@dataclass
class WeatherCircle:
    message: str
    cod: int
    count: int
    list: List[ListElement]

    @staticmethod
    def from_dict(obj: Any) -> 'WeatherCircle':
        assert isinstance(obj, dict)
        message = from_str(obj.get("message"))
        cod = int(from_str(obj.get("cod")))
        count = from_int(obj.get("count"))
        list = from_list(ListElement.from_dict, obj.get("list"))
        return WeatherCircle(message, cod, count, list)

    def to_dict(self) -> dict:
        result: dict = {}
        result["message"] = from_str(self.message)
        result["cod"] = from_str(str(self.cod))
        result["count"] = from_int(self.count)
        result["list"] = from_list(lambda x: to_class(ListElement, x), self.list)
        return result


def weather_circle_from_dict(s: Any) -> WeatherCircle:
    return WeatherCircle.from_dict(s)


def weather_circle_to_dict(x: WeatherCircle) -> Any:
    return to_class(WeatherCircle, x)
