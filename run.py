import os

import asyncio
from dotenv import load_dotenv

from aiogram import Bot, Dispatcher, F
from aiogram.types import Message
from aiogram.filters import CommandStart, Command


dp = Dispatcher()


@dp.message(Command('help'))
async def cmd_help(message: Message):
    await message.answer('Тут должна быть помощь')

@dp.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer('Привет')

@dp.message(F.text.lower() == "привет")
async def hello(message: Message):
    await message.reply('Привет. Как дела?')

@dp.message(F.photo)    #хендлер работы с фото
async def handle_photo(message: Message):
    file_id = message.photo[-1].file_id
    await message.answer_photo(file_id, caption='Вот твоё фото')

@dp.message(F.video)
async def handle_video(message: Message):
    file_id = message.video.file_id
    await message.answer_video(file_id, caption='Вот твоё видео')

@dp.message(F.voice)
async def handle_voice(message: Message):
    file_id = message.voice.file_id
    await message.answer_voice(file_id, caption='Вот твоя голосовуха')

@dp.message(F.sticker)  #обработчик стикера
async def handle_sticker(message: Message):
    file_id = message.sticker.file_id
    await  message.answer_sticker(file_id)


@dp.message()
async def echo(message: Message):
    await message.answer(message.text)





async def startup(dispatcher: Dispatcher):
    print('Бот запущен')

async def shutdown(dispatcher: Dispatcher):
    print('Бот остановлен')

async def main():
    load_dotenv()
    bot = Bot(token=os.getenv('TOKEN_TBOT'))
    dp.startup.register(startup)
    dp.shutdown.register(shutdown)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
