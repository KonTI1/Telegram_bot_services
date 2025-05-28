## Функции

- Конвертация валют
- Генерация случайных паролей
- Получение текущей погоды по городу
- Получение информации по IP-адресу

## Как запустить

1. Склонируйте репозиторий:

- git clone https://github.com/KonTI1/Telegram_bot_services.git
- cd Telegram_bot_services

2. Создайте и активируйте виртуальное окружение (рекомендуется):

- python -m venv venv
- source venv/bin/activate  # Linux/Mac
- venv\Scripts\activate     # Windows

3. Установите зависимости:

- pip install -r requirements.txt

4. Создайте файл .env в корне проекта и добавьте необходимые переменные:

- BOT_TOKEN=ваш_токен_бота
- WEATHER_API_KEY=ключ_openweathermap
- CURRENCY_API_KEY=ключ_для_конвертации_валют

5. Запустите бота:

- python bot.py
