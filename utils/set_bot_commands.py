from aiogram import types


async def set_default_commands(dp):
    await dp.bot.set_my_commands(
        [
            types.BotCommand("start", "Запустити бота"),
            types.BotCommand("help", "Вивести команду"),
            types.BotCommand("create_wheel", "Створити колесо"),
            types.BotCommand("update_wheel", "Оновити колесо"),
            types.BotCommand("edit_wheel", "Змінити колесо"),
            types.BotCommand("drop_wheel", "Очистити колесо"),
            types.BotCommand("show_wheel", "Показати колесо"),
        ]
    )
