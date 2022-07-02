from aiogram import types

from loader import dp, db
from keyboards.default import help_keyboard

from states import Steps


@dp.message_handler(commands=['show_wheel'], state=Steps.defaultState)
async def show_wheel(message: types.Message):
    categories = await db.select_categories(message.from_user.id)
    sm = [categories['category_careers'],
          categories['category_family'],
          categories['category_environment'],
          categories['category_health_sport'],
          categories['category_education'],
          categories['category_hobbies'],
          categories['category_rest']
          ]
    amount = sum(sm)
    if amount == 0:
        amount = 7
    await message.answer(
        f"""
        Ваше колесо витрат:
🤵Кар'єра ~ {round(categories['category_careers']/amount * 100, 2)}% ({categories['category_careers']} грн)
👪Сім'я ~ {round(categories['category_family']/amount * 100, 2)}% ({categories['category_family']} грн)
🍂Оточення ~ {round(categories['category_environment']/amount * 100, 2)}% ({categories['category_environment']} грн)
🏐Здоров'я, спорт ~ {round(categories['category_health_sport']/amount * 100, 2)}% ({categories['category_health_sport']} грн)
👨‍🎓Розвиток(освіта) ~ {round(categories['category_education']/amount * 100, 2)}% ({categories['category_education']} грн)
🎨Творчіст і хоббі ~ {round(categories['category_hobbies']/amount * 100, 2)}% ({categories['category_hobbies']} грн)
🧭Відпочинок та подорожі ~ {round(categories['category_rest']/amount * 100, 2)}% ({categories['category_rest']} грн)"""
    )
    accord = {
        'category_careers': "Кар'єра",
        'category_family': "Сім'я",
        'category_environment': "Оточення",
        'category_health_sport': "Здоров'я, спорт",
        'category_education': "Розвиток(освіта)",
        'category_hobbies': "Творчіст і хоббі",
        'category_rest': "Відпочинок та подорожі"
    }
    mn = min(sm)
    mx = max(sm)
    min_label = []
    max_label = []
    for key, val in categories.items():
        if val == mn:
            min_label.append(accord[key])
        if val == mx:
            max_label.append(accord[key])
    if mx != 0:
        await message.answer(f'Зверніть увагу на найменші витрати в таких категоріях:\n{", ".join(min_label)}')
        await message.answer(f'Зверніть увагу на найбільші витрати в таких категоріях:\n{", ".join(max_label)}')
        await message.answer('Намагайтесь їх балансувати!', reply_markup=help_keyboard)
    else:
        await message.answer('Заповніть колесо!')
