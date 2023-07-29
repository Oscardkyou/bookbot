import random
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.types import ParseMode
from aiogram.utils import executor


logging.basicConfig(level=logging.INFO)
dp = Dispatcher(bot)

def generate_random_number():
    return random.randint(1, 100)

@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.reply("Привет! Я бот, который угадывает число от 1 до 100. Загадай число, а я попробую его угадать.")

@dp.message_handler(content_types=types.ContentType.TEXT)
async def guess_number(message: types.Message):
    if message.text.isdigit():
        user_number = int(message.text)
        bot_number = generate_random_number()

        if user_number < bot_number:
            await message.reply("Мое число больше.")
        elif user_number > bot_number:
            await message.reply("Мое число меньше.")
        else:
            await message.reply("Угадал! Мое число было {}.".format(bot_number))
    else:
        await message.reply("Пожалуйста, введите число от 1 до 100.")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
