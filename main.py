import asyncio

from aiogram import Bot, Dispatcher, types

from os import environ
from dotenv import load_dotenv

load_dotenv()

TELEGRAM_TOKEN = environ['TELEGRAM_TOKEN']


bot = Bot(token=TELEGRAM_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup()
    registration_button = types.KeyboardButton(text='Регистрация')
    timetable_button = types.KeyboardButton(text='Расписание')
    chat_button = types.KeyboardButton(text='Чат')
    speakers_button = types.KeyboardButton(text='Спикеры')
    site_button = types.KeyboardButton(text='Сайт церкви')

    keyboard.row(registration_button, timetable_button)
    keyboard.row(chat_button, speakers_button)
    keyboard.row(site_button)

    await message.reply("Привет!\nНапиши мне что-нибудь!",
                        reply_markup=keyboard)


@dp.message_handler(lambda message: message.text == "Регистрация")
async def registration(message: types.Message):
    pass


@dp.message_handler(lambda message: message.text == "Расписание")
async def timetable(message: types.Message):
    pass


@dp.message_handler(lambda message: message.text == "Чат")
async def chat(message: types.Message):
    pass


@dp.message_handler(lambda message: message.text == "Спикеры")
async def speakers(message: types.Message):
    pass


@dp.message_handler(lambda message: message.text == "Сайт церкви")
async def church_site(message: types.Message):
    pass


async def main():
    print('Bot started')
    await dp.skip_updates()  # Пропускаем все сообщения, которые приходили до запуска
    await dp.start_polling()  # Начинаем опрос приходящих сообщений с API бота


if __name__ == '__main__':
    asyncio.run(main())
