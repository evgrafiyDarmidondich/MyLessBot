import asyncio
from pyexpat.errors import messages

from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.filters import CommandStart

from config import TOKEN_TBOT

bot = Bot(token=TOKEN_TBOT)
dp = Dispatcher()


@dp.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer('Привет')

@dp.message()
async def echo(message: Message):
    await message.answer(message.text)


async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
