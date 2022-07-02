from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

request_contact = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Надіслати контакт", request_contact=True)
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)

categories = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Кар'єра🤵"),
            KeyboardButton(text="Сім'я👪"),
        ],
        [
            KeyboardButton(text="Оточення🍂"),
            KeyboardButton(text="Здоров'я, спорт🏐"),
        ],
        [
            KeyboardButton(text="Розвиток (освіта)👨‍🎓"),
        ],
        [
            KeyboardButton(text="Творчість і хоббі🎨"),
        ],
        [
            KeyboardButton(text="Відпочинок та подорожі🧭"),
        ],
        [
            KeyboardButton(text="Готово✅"),
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)

help_keyboard = ReplyKeyboardMarkup(
    keyboard=[[KeyboardButton(text="/help")]], resize_keyboard=True,
)
