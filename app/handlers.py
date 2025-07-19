import asyncio
from os.path import defpath, split

from aiogram import Router, F
from aiogram.filters import Command, CommandStart
from aiogram.types import Message, CallbackQuery, KeyboardButton
from aiogram.enums import ChatAction
from aiogram.utils.keyboard import ReplyKeyboardBuilder

import app.keybords as kb
import app.builder as bui

router = Router()



@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.bot.send_chat_action(chat_id=message.from_user.id, action=ChatAction.TYPING)
    await asyncio.sleep(1)
    await message.answer('Привет', reply_markup=kb.inline_main)


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

# Обработчик келлбеков
@router.callback_query(F.data == 'catalog')
async def get_catalog(calldack: CallbackQuery):
    # await calldack.answer('Вы выбрали каталог', show_alert=True) #показывает всплывающее окно
    await calldack.answer('Вы выбрали каталог') #Пишет вв верху
    await calldack.message.edit_text('Выберете категорию', reply_markup=await kb.catalog_builder()) # Отправляет сообщение и клавиатуру

@router.callback_query(F.data == 'item_Nike')
async def get_nike(callback: CallbackQuery):
    await callback.answer(f"Вы выбрали {callback.data}")
    await callback.message.edit_text(f"Вы выбрали {callback.data}", reply_markup=kb.back)

@router.callback_query(F.data == 'item_Adidas')
async def get_nike(callback: CallbackQuery):
    print(callback.data)
    await callback.answer(f"Вы выбрали {callback.data}")
    await callback.message.edit_text(f"Вы выбрали {callback.data}", reply_markup=kb.back)

@router.callback_query(F.data == 'item_rebook')
async def get_nike(callback: CallbackQuery):
    await callback.answer(f"Вы выбрали {callback.data}")
    await callback.message.edit_text(f"Вы выбрали {callback.data}", reply_markup=kb.back)

@router.callback_query(F.data == 'menu')
async def cmd_start(callback: CallbackQuery):
    await callback.answer('Меню')
    await callback.message.edit_text('Меню', reply_markup=kb.inline_main)