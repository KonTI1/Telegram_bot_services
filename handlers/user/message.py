import html

from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import Command, CommandStart
from aiogram.fsm.context import FSMContext
from core.States import States

from services.currency import currency
from services.ipinfo import get_ip_info
from services.weather import get_weather
from keyboard.keyboards import start_menu as kb


router = Router()

async def start_handler(message: Message):
    user_name = html.escape(message.from_user.first_name or "Пользователь")
    text = (
        f"👋 Добрый день, <b>{user_name}</b>!\n\n"
        "Рад видеть вас здесь! 😊\n"
        "Пожалуйста, выберите, что хотите узнать:"
    )
    await message.answer(text, reply_markup=kb)


async def get_weather(message: Message, state: FSMContext):
    city = message.text
    await message.answer(await get_weather(city))
    await state.clear()
    
async def get_currency(message: Message, state: FSMContext):
    msg = message.text.split()
    amount = int(msg[0])
    param1 = msg[1].upper()
    param2 = msg[3].upper()
    await message.answer(await currency(param1, param2,amount))
    await state.clear()

async def ip_info(message: Message, state: FSMContext):
    ip = message.text
    await message.answer(str(await get_ip_info(ip)))
    await state.clear()

def register_handlers():
    router.message.register(get_weather, States.weather)
    router.message.register(start_handler, CommandStart())
    router.message.register(get_currency, States.currency)
    router.message.register(ip_info, States.ip)
