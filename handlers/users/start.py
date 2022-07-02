from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from loader import dp, db
from keyboards.default import request_contact
from aiogram.types import ContentTypes
from states import Steps


@dp.message_handler(CommandStart(), state=None)
async def bot_start(message: types.Message):
        await Steps.regState.set()
        await message.answer(f"Привіт!\nЯ бот, який допоможе тобі зібрати всі цінності твого життя і поєднати їх з твоїми фінансами.")
        await message.answer('Щоб зареєструватися, відправте свій контакт', reply_markup=request_contact)


@dp.message_handler(content_types=ContentTypes.CONTACT, state=Steps.regState)
async def bot_name_ask(message: types.Message):
    try:
        await db.insert_table_user(message.contact.user_id, message.contact.first_name, message.contact.phone_number)
        await message.answer(f'Окей, ви зареєстровані!')
        await message.answer('Для початку роботи потрібно створити колесо: /create_wheel')
        await Steps.defaultState.set()
    except:
        await message.answer(f'Ви вже зареєстровані :)')
        await message.answer('/help - показати команди')
        await Steps.defaultState.set()


