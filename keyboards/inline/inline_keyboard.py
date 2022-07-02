from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

confirm_request = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Так', callback_data='Так'),
            InlineKeyboardButton(text='Ні', callback_data='Ні')
        ]
    ]
)
