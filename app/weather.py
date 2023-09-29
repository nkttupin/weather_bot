import json
import aiohttp
import asyncio
from dotenv import load_dotenv
import os

load_dotenv()


async def fetch_weather_data():
    url = f"https://api.openweathermap.org/data/2.5/weather?lat=58.60472&lon=49.65642&appid={os.getenv('OPEN_WEATHER_TOKEN')}"

    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            data = await response.json()

    return data


async def get_weather():
    data = await fetch_weather_data()

    coord_lon = data['coord']['lon']
    coord_lat = data['coord']['lat']
    weather_description = data['weather'][0]['description']
    main_temp = data['main']['temp']
    main_humidity = data['main']['humidity']
    wind_speed = data['wind']['speed']

    result = [
        f"Широта: {coord_lat}",
        f"Долгота: {coord_lon}",
        f"Описание погоды: {weather_description}",
        f"Температура: {round(main_temp-273.15, 2)}°C",
        f"Влажность: {main_humidity}",
        f"Скорость ветра: {wind_speed}"
    ]

    return '\n'.join(result)


if __name__ == '__main__':
    asyncio.run(get_weather())
