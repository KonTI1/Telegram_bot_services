import aiohttp

from core.config import Settings

settings = Settings()


async def get_ip_info(ip: str) -> str:
    url = f"http://ip-api.com/json/{ip}"
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as resp:
                data = await resp.json()
        text = (
            f"🌐IP: <code>{ip}</code>\n"
            f"🏳️Страна: {data['country']}\n"
            f"🏙️Регион: {data['regionName']}\n"
            f"🏢Город: {data['city']}\n"
            f"📶Провайдер: {data['isp']}\n"
            f"📍Координаты: {data['lat']}, {data['lon']}\n"
            f"⏰Временная зона: {data['timezone']}\n"
            f"🏛️Организация: {data['org']}"
        )
        return text
    except Exception as e:
        print(e)
        return "❌ Произошла ошибка при получении информации о IP-адресе."