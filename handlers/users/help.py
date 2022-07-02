from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp

from loader import dp


@dp.message_handler(CommandHelp(), state="*")
async def bot_help(message: types.Message):
    text = ("Список команд: ",
            "/start - Почати працювати",
            "/help - Отримати цей список",
            "/create_wheel - Створити колесо",
            "/update_wheel - Оновити колесо",
            "/edit_wheel - Змінити колесо",
            "/drop_wheel - Очистити колесо",
            "/show_wheel - Вивести колесо")
    
    await message.answer("\n".join(text))
