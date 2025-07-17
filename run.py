import os

import asyncio
from dotenv import load_dotenv

from aiogram import Bot, Dispatcher, F

from handlers import router


async def main():
    load_dotenv()
    bot = Bot(token=os.getenv('TOKEN_TBOT'))
    dp = Dispatcher()
    dp.startup.register(startup)
    dp.shutdown.register(shutdown)
    dp.include_router(router)
    await dp.start_polling(bot)


async def startup(dispatcher: Dispatcher):
    print('Бот запущен')

async def shutdown(dispatcher: Dispatcher):
    print('Бот остановлен')

if __name__ == "__main__":
    asyncio.run(main())
