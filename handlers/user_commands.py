import asyncio
import logging
from os import getenv
from typing import Any, Dict
from aiogram import Router, Bot, Dispatcher, F, types
from aiogram.types import Message, ReplyKeyboardMarkup, ReplyKeyboardRemove
from aiogram.filters import CommandStart, Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
import text
import keyboards
from keyboards import reply

router = Router()
dp = Dispatcher()

@router.message(Command(commands=["start"]))
async def command_start(message: Message):
    await message.answer(text.salam, reply_markup=reply.main_kb)

@router.message(F.text == "О НАС НАФИГ")
async def greet_user(message: types.Message):
    await message.answer(text.lozhka)

@dp.message()  # Все остальные сообщения
async def gavno(message: Message):
    await message.answer("Извините, я не понимаю вас. Пожалуйста, попробуйте задать другой вопрос.")

    
