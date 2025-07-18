import asyncio
from aiogram import Router, F
from aiogram.filters import Command, CommandStart
from aiogram.types import Message
from aiogram.enums import ChatAction

import app.keybords as kb

router = Router()



@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.bot.send_chat_action(chat_id=message.from_user.id, action=ChatAction.TYPING)
    await asyncio.sleep(1)
    await message.answer('Привет', reply_markup=kb.main)

@router.message(Command('help'))
async def cmd_help(message: Message):
    await message.answer('Тут должна быть помощь')

@router.message(F.text.lower() == "привет")
async def hello(message: Message):
    await message.bot.send_chat_action(chat_id=message.from_user.id, action=ChatAction.TYPING)
    await asyncio.sleep(2)
    await message.reply('Привет. Как дела?')

@router.message(F.photo)    #хендлер работы с фото
async def handle_photo(message: Message):
    file_id = message.photo[-1].file_id
    await message.bot.send_chat_action(chat_id=message.from_user.id, action=ChatAction.UPLOAD_PHOTO)
    await asyncio.sleep(2)
    await message.answer_photo(file_id, caption='Вот твоё фото')

@router.message(F.video)
async def handle_video(message: Message):
    file_id = message.video.file_id
    await message.bot.send_chat_action(chat_id=message.from_user.id, action=ChatAction.UPLOAD_VIDEO)
    await asyncio.sleep(2)
    await message.answer_video(file_id, caption='Вот твоё видео')

@router.message(F.voice)
async def handle_voice(message: Message):
    file_id = message.voice.file_id
    await message.answer_voice(file_id, caption='Вот твоя голосовуха')

@router.message(F.sticker)  #обработчик стикера
async def handle_sticker(message: Message):
    file_id = message.sticker.file_id
    await  message.answer_sticker(file_id)

@router.message(F.text.lower() == "проверка роутера")
async def check_router(message: Message):
    await message.answer('всё ок')

@router.message(Command('adminlist'))
async def admin_list(message: Message):
    list_admin = await message.bot.get_chat_administrators(chat_id=-1002880973296)
    for u in list_admin:
        user = u.user.id , u.user.first_name
        await message.answer(f"id: {user[0]}\nИмя: {user[1]}")