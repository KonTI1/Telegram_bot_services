import aiohttp
from core.config import Settings

settings = Settings()

async def currency(param1, param2, amount: float):
    url = f"https://v6.exchangerate-api.com/v6/{settings.currency_api_key}/pair/{param1}/{param2}/{amount}"
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as r:
                data = await r.json()
                result = data["conversion_result"]
                rate = data["conversion_rate"]
                update = data["time_last_update_utc"]

                return (
                    f"💸 <b>Конвертация валют</b>\n\n"
                    f"{amount:.2f} {param1.upper()} = {result:.2f} {param2.upper()}\n"
                    f"💱 Курс: 1 {param1.upper()} = {rate:.2f} {param2.upper()}\n"
                    f"📅 Обновлено: {update}\n"
                    f"👀 Источник: ExchangeRate-API"
                )
    except Exception as e:
        print(e)
        return (
            "⚠️ Произошла ошибка при получении курса валюты. "
            "Проверьте правильность введённых кодов валют (например, USD, EUR)."
        )