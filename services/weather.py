import aiohttp

from core.config import Settings

settings = Settings()

async def get_weather(city: str) -> dict:
    url = f"https://api.openweathermap.org/data/2.5/weather"
    params={
            "q": city,
            "appid": settings.weather_api_key,
            "units": "metric",
            "lang": "ru"
        }
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url, params=params) as repo:    
                data = await repo.json()
                city = data.get('name')
                weather_main = data['weather'][0]['main']
                weather_desc = data['weather'][0]['description'].capitalize()
                temp = data['main']['temp']
                feels_like = data['main']['feels_like']
                humidity = data['main']['humidity']
                wind_speed = data['wind']['speed']

                text = (
                    f"🌆 *Город:* {city}\n"
                    f"🌤 *Погода:* {weather_main} — _{weather_desc}_\n"
                    f"🌡 *Температура:* {temp}°C (ощущается как {feels_like}°C)\n"
                    f"💧 *Влажность:* {humidity}%\n"
                    f"💨 *Ветер:* {wind_speed} м/с\n"
                )
                return text
    except Exception as e:
        print("Ошибка запроса:")
        return {}
