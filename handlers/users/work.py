from aiogram import types
import re
from loader import bot, dp, db
from keyboards.default import categories, help_keyboard
from keyboards.inline import confirm_request
from aiogram.types import ContentTypes
from states import Steps


@dp.message_handler(commands=['create_wheel'], state=Steps.defaultState)
async def create_wheel(message: types.Message):
    try:
        await db.drop_wheel(message.from_user.id)
    except:
        pass
    await message.answer(f'Давай заповнимо поля твого колеса життєвого балансу.\nОбирай категорію.', reply_markup=categories)
    await Steps.wheel_updatingState.set()


@dp.message_handler(text="Готово✅", state=Steps.wheel_updatingState)
async def updating_wheel(message: types.Message):
    await message.answer("Колесо готове, /help - команди.", reply_markup=help_keyboard)
    await Steps.defaultState.set()


#  wheel create {
@dp.message_handler(content_types=ContentTypes.TEXT, state=Steps.wheel_updatingState)
async def updating_wheel(message: types.Message):
    await message.answer(f'Чудово, тепер вкажи суму витрат(зберігається у грн) та дату\n(у вигляді "витрати, рік-місяць-день") за цією категорією - {message.text}\n (Якщо випадково вибрана не та категорія, введіть "0")')
    if message.text == "Кар'єра🤵":
        await Steps.set_career_valueState.set()
    elif message.text == "Сім'я👪":
        await Steps.set_family_valueState.set()
    elif message.text == "Оточення🍂":
        await Steps.set_environment_valueState.set()
    elif message.text == "Здоров'я, спорт🏐":
        await Steps.set_health_valueState.set()
    elif message.text == "Розвиток (освіта)👨‍🎓":
        await Steps.set_education_valueState.set()
    elif message.text == "Творчість і хоббі🎨":
        await Steps.set_hobbies_valueState.set()
    elif message.text == "Відпочинок та подорожі🧭":
        await Steps.set_rest_valueState.set()
    else:
        await message.answer('Невірно введені дані.')


@dp.message_handler(content_types=ContentTypes.TEXT, state=Steps.set_career_valueState)
async def updating_wheel(message: types.Message):
    try:
        await db.update_careers_category(message.from_user.id, message.text.split(',')[0])
        await message.answer(f'Чудово!\nТепер інша категорія або "Готово✅"', reply_markup=categories)
        await Steps.wheel_updatingState.set()
    except:
        await message.answer('Невірно введені дані.')


@dp.message_handler(content_types=ContentTypes.TEXT, state=Steps.set_family_valueState)
async def updating_wheel(message: types.Message):
    try:
        await db.update_family_category(message.from_user.id, message.text.split(',')[0])
        await message.answer(f'Чудово!\nТепер інша категорія або "Готово✅"', reply_markup=categories)
        await Steps.wheel_updatingState.set()
    except:
        await message.answer('Невірно введені дані.')


@dp.message_handler(content_types=ContentTypes.TEXT, state=Steps.set_environment_valueState)
async def updating_wheel(message: types.Message):
    try:
        await db.update_environment_category(message.from_user.id, message.text.split(',')[0])
        await message.answer(f'Чудово!\nТепер інша категорія або "Готово✅"', reply_markup=categories)
        await Steps.wheel_updatingState.set()
    except:
        await message.answer('Невірно введені дані.')


@dp.message_handler(content_types=ContentTypes.TEXT, state=Steps.set_hobbies_valueState)
async def updating_wheel(message: types.Message):
    try:
        await db.update_hobbies_category(message.from_user.id, message.text.split(',')[0])
        await message.answer(f'Чудово!\nТепер інша категорія або "Готово✅"', reply_markup=categories)
        await Steps.wheel_updatingState.set()
    except:
        await message.answer('Невірно введені дані.')


@dp.message_handler(content_types=ContentTypes.TEXT, state=Steps.set_rest_valueState)
async def updating_wheel(message: types.Message):
    try:
        await db.update_rest_category(message.from_user.id, message.text.split(',')[0])
        await message.answer(f'Чудово!\nТепер інша категорія або "Готово✅"', reply_markup=categories)
        await Steps.wheel_updatingState.set()
    except:
        await message.answer('Невірно введені дані.')


@dp.message_handler(content_types=ContentTypes.TEXT, state=Steps.set_education_valueState)
async def updating_wheel(message: types.Message):
    try:
        await db.update_education_category(message.from_user.id, message.text.split(',')[0])
        await message.answer(f'Чудово!\nТепер інша категорія або "Готово✅"', reply_markup=categories)
        await Steps.wheel_updatingState.set()
    except:
        await message.answer('Невірно введені дані.')


@dp.message_handler(content_types=ContentTypes.TEXT, state=Steps.set_health_valueState)
async def updating_wheel(message: types.Message):
    try:
        await db.update_health_category(message.from_user.id, message.text.split(',')[0])
        await message.answer(f'Чудово!\nТепер інша категорія або "Готово✅"', reply_markup=categories)
        await Steps.wheel_updatingState.set()
    except:
        await message.answer('Невірно введені дані.')
#  wheel create }


#  wheel update {
@dp.message_handler(commands=['update_wheel'], state=Steps.defaultState)
async def create_wheel(message: types.Message):
    await message.answer(f'Додаємо фінанси до колеса життєвого балансу.\nОбирай категорію.', reply_markup=categories)
    await Steps.wheel_updatingState.set()


@dp.message_handler(content_types=ContentTypes.TEXT, state=Steps.wheel_updatingState)
async def updating_wheel(message: types.Message):
    await message.answer(f'Чудово, тепер вкажи суму витрат(зберігається у грн) та дату\n(у вигляді "витрати, рік-місяць-день") за цією категорією - {message.text}\n (Якщо випадково вибрана не та категорія, введіть "0")')
    if message.text == "Кар'єра🤵":
        await Steps.set_career_valueState.set()
    elif message.text == "Сім'я👪":
        await Steps.set_family_valueState.set()
    elif message.text == "Оточення🍂":
        await Steps.set_environment_valueState.set()
    elif message.text == "Здоров'я, спорт🏐":
        await Steps.set_health_valueState.set()
    elif message.text == "Розвиток (освіта)👨‍🎓":
        await Steps.set_education_valueState.set()
    elif message.text == "Творчість і хоббі🎨":
        await Steps.set_hobbies_valueState.set()
    elif message.text == "Відпочинок та подорожі🧭":
        await Steps.set_rest_valueState.set()
    else:
        await message.answer('Невірно введені дані.')


@dp.message_handler(content_types=ContentTypes.TEXT, state=Steps.set_career_valueState)
async def updating_wheel(message: types.Message):
    try:
        await db.update_careers_category(message.from_user.id, message.text.split(',')[0])
        await message.answer(f'Чудово!\nТепер інша категорія або "Готово✅"', reply_markup=categories)
        await Steps.wheel_updatingState.set()
    except:
        await message.answer('Невірно введені дані.')


@dp.message_handler(content_types=ContentTypes.TEXT, state=Steps.set_family_valueState)
async def updating_wheel(message: types.Message):
    try:
        await db.update_family_category(message.from_user.id, message.text.split(',')[0])
        await message.answer(f'Чудово!\nТепер інша категорія або "Готово✅"', reply_markup=categories)
        await Steps.wheel_updatingState.set()
    except:
        await message.answer('Невірно введені дані.')


@dp.message_handler(content_types=ContentTypes.TEXT, state=Steps.set_environment_valueState)
async def updating_wheel(message: types.Message):
    try:
        await db.update_environment_category(message.from_user.id, message.text.split(',')[0])
        await message.answer(f'Чудово!\nТепер інша категорія або "Готово✅"', reply_markup=categories)
        await Steps.wheel_updatingState.set()
    except:
        await message.answer('Невірно введені дані.')


@dp.message_handler(content_types=ContentTypes.TEXT, state=Steps.set_hobbies_valueState)
async def updating_wheel(message: types.Message):
    try:
        await db.update_hobbies_category(message.from_user.id, message.text.split(',')[0])
        await message.answer(f'Чудово!\nТепер інша категорія або "Готово✅"', reply_markup=categories)
        await Steps.wheel_updatingState.set()
    except:
        await message.answer('Невірно введені дані.')


@dp.message_handler(content_types=ContentTypes.TEXT, state=Steps.set_rest_valueState)
async def updating_wheel(message: types.Message):
    try:
        await db.update_rest_category(message.from_user.id, message.text.split(',')[0])
        await message.answer(f'Чудово!\nТепер інша категорія або "Готово✅"', reply_markup=categories)
        await Steps.wheel_updatingState.set()
    except:
        await message.answer('Невірно введені дані.')


@dp.message_handler(content_types=ContentTypes.TEXT, state=Steps.set_education_valueState)
async def updating_wheel(message: types.Message):
    try:
        await db.update_education_category(message.from_user.id, message.text.split(',')[0])
        await message.answer(f'Чудово!\nТепер інша категорія або "Готово✅"', reply_markup=categories)
        await Steps.wheel_updatingState.set()
    except:
        await message.answer('Невірно введені дані.')


@dp.message_handler(content_types=ContentTypes.TEXT, state=Steps.set_health_valueState)
async def updating_wheel(message: types.Message):
    try:
        await db.update_health_category(message.from_user.id, message.text.split(',')[0])
        await message.answer(f'Чудово!\nТепер інша категорія або "Готово✅"', reply_markup=categories)
        await Steps.wheel_updatingState.set()
    except:
        await message.answer('Невірно введені дані.')
#  wheel update }


#  wheel edit {
@dp.message_handler(commands=['edit_wheel'], state=Steps.defaultState)
async def create_wheel(message: types.Message):
    await message.answer(f'Задаємо нове значення для колеса життєвого балансу.\nОбирай категорію.', reply_markup=categories)
    await Steps.wheel_editingState.set()


@dp.message_handler(text="Готово✅", state=Steps.wheel_editingState)
async def updating_wheel(message: types.Message):
    await message.answer("Колесо змінено, /help - команди.", reply_markup=help_keyboard)
    await Steps.defaultState.set()


@dp.message_handler(content_types=ContentTypes.TEXT, state=Steps.wheel_editingState)
async def updating_wheel(message: types.Message):
    await message.answer(f'Чудово, тепер вкажи суму витрат(зберігається у грн) та дату\n(у вигляді "витрати, рік-місяць-день") за цією категорією - {message.text}\n')
    if message.text == "Кар'єра🤵":
        await Steps.edit_career_valueState.set()
    elif message.text == "Сім'я👪":
        await Steps.edit_family_valueState.set()
    elif message.text == "Оточення🍂":
        await Steps.edit_environment_valueState.set()
    elif message.text == "Здоров'я, спорт🏐":
        await Steps.edit_health_valueState.set()
    elif message.text == "Розвиток (освіта)👨‍🎓":
        await Steps.edit_education_valueState.set()
    elif message.text == "Творчість і хоббі🎨":
        await Steps.edit_hobbies_valueState.set()
    elif message.text == "Відпочинок та подорожі🧭":
        await Steps.edit_rest_valueState.set()
    else:
        await message.answer('Невірно введені дані.')


@dp.message_handler(content_types=ContentTypes.TEXT, state=Steps.edit_career_valueState)
async def updating_wheel(message: types.Message):
    try:
        await db.edit_careers_category(message.from_user.id, message.text.split(',')[0])
        await message.answer(f'Чудово!\nТепер інша категорія або "Готово✅"', reply_markup=categories)
        await Steps.wheel_editingState.set()
    except:
        await message.answer('Невірно введені дані.')


@dp.message_handler(content_types=ContentTypes.TEXT, state=Steps.edit_family_valueState)
async def updating_wheel(message: types.Message):
    try:
        await db.edit_family_category(message.from_user.id, message.text.split(',')[0])
        await message.answer(f'Чудово!\nТепер інша категорія або "Готово✅"', reply_markup=categories)
        await Steps.wheel_editingState.set()
    except:
        await message.answer('Невірно введені дані.')


@dp.message_handler(content_types=ContentTypes.TEXT, state=Steps.edit_environment_valueState)
async def updating_wheel(message: types.Message):
    try:
        await db.edit_environment_category(message.from_user.id, message.text.split(',')[0])
        await message.answer(f'Чудово!\nТепер інша категорія або "Готово✅"', reply_markup=categories)
        await Steps.wheel_editingState.set()
    except:
        await message.answer('Невірно введені дані.')


@dp.message_handler(content_types=ContentTypes.TEXT, state=Steps.edit_hobbies_valueState)
async def updating_wheel(message: types.Message):
    try:
        await db.edit_hobbies_category(message.from_user.id, message.text.split(',')[0])
        await message.answer(f'Чудово!\nТепер інша категорія або "Готово✅"', reply_markup=categories)
        await Steps.wheel_editingState.set()
    except:
        await message.answer('Невірно введені дані.')


@dp.message_handler(content_types=ContentTypes.TEXT, state=Steps.edit_rest_valueState)
async def updating_wheel(message: types.Message):
    try:
        await db.edit_rest_category(message.from_user.id, message.text)
        await message.answer(f'Чудово!\nТепер інша категорія або "Готово✅"', reply_markup=categories)
        await Steps.wheel_editingState.set()
    except:
        await message.answer('Невірно введені дані.')


@dp.message_handler(content_types=ContentTypes.TEXT, state=Steps.edit_education_valueState)
async def updating_wheel(message: types.Message):
    try:
        await db.edit_education_category(message.from_user.id, message.text.split(',')[0])
        await message.answer(f'Чудово!\nТепер інша категорія або "Готово✅"', reply_markup=categories)
        await Steps.wheel_editingState.set()
    except:
        await message.answer('Невірно введені дані.')


@dp.message_handler(content_types=ContentTypes.TEXT, state=Steps.edit_health_valueState)
async def updating_wheel(message: types.Message):
    try:
        await db.edit_health_category(message.from_user.id, message.text.split(',')[0])
        await message.answer(f'Чудово!\nТепер інша категорія або "Готово✅"', reply_markup=categories)
        await Steps.wheel_editingState.set()
    except:
        await message.answer('Невірно введені дані.')
#  wheel edit }


#  wheel drop {
@dp.message_handler(commands=['drop_wheel'], state=Steps.defaultState)
async def drop_wheel(message: types.Message):
    await message.answer(f'Ви впевнені, що хочете очистити своє колесо?', reply_markup=confirm_request)
    await Steps.confirmState.set()


@dp.callback_query_handler(text="Так", state=Steps.confirmState)
async def bot_drop_wheel(callback: types.callback_query):
    await db.drop_wheel(callback.from_user.id)
    await bot.send_message(callback.from_user.id, "Колесо очищене. /help - команди.", reply_markup=help_keyboard)
    await Steps.defaultState.set()


@dp.callback_query_handler(text="Ні", state=Steps.confirmState)
async def bot_drop_wheel(callback: types.callback_query):
    await bot.send_message(callback.from_user.id, "Очищення відмінене. /help - команди.", reply_markup=help_keyboard)
    await Steps.defaultState.set()
#  wheel drop }
