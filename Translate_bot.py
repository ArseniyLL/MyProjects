# - *- coding: utf- 8 - *-
import googletrans
import config
from aiogram import Bot, Dispatcher, executor, types


bot = Bot(config.token)
dp = Dispatcher(bot)
translator = googletrans.Translator()


@dp.message_handler(commands=['start'])
async def start(message : types.Message):
    await bot.send_message(message.from_user.id, '<b><u>Привет, я бот переводчик с английского на русский</u></b>', parse_mode=types.ParseMode.HTML)


@dp.message_handler()
async def echo(message : types.Message):
    translator.detect(message.text)
    text = translator.translate(message.text, src='en', dest='ru').text
    await message.reply(text)


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
    