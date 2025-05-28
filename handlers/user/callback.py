import html

from aiogram import Router, F
from aiogram.types import CallbackQuery
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext

from core.States import States
from services.password import generate_password

router = Router()

async def weather(callback: CallbackQuery, state: FSMContext):
    await state.set_state(States.weather)
    await callback.message.answer("Введите название города")
    
async def currency(callback: CallbackQuery, state: FSMContext):
    await state.set_state(States.currency)
    await callback.message.answer("Введите название валюты:\n\n Пример: 1 USD to RUB")

async def ip_info(callback: CallbackQuery, state: FSMContext):
    await state.set_state(States.ip)
    await callback.message.answer("Введите IP адрес\n\n Пример: 237.84.2.178")

async def get_password(callback: CallbackQuery, state: FSMContext):
    await callback.message.answer(f"Вот ваш пароль: <code>{generate_password()}</code>")


def register_handlers():
    router.callback_query.register(weather, F.data == 'weather')
    router.callback_query.register(currency, F.data == 'currency')
    router.callback_query.register(ip_info, F.data == 'ip')
    router.callback_query.register(get_password, F.data == 'password')