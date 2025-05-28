from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


start_menu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="🌤️☀️🌧️ Погода", callback_data="weather"),
            InlineKeyboardButton(text="🔑🛡️ Генератор случайного пароля", callback_data="password")
        ],
        [
            InlineKeyboardButton(text="💱💰 Калькулятор валют", callback_data="currency"),
            InlineKeyboardButton(text="📡🖥️ Инфо по ip", callback_data="ip")
        ]
    ]
)
