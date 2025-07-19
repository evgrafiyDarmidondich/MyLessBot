from aiogram.types import KeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder

keys = ['Каталог', 'Корзина', 'Контакты']

async def menu_builder():
    keyboard = ReplyKeyboardBuilder()
    for key1 in keys:
        keyboard.add(KeyboardButton(text=key1))
    keyboard.adjust(2)
    return keyboard.as_markup()


# from aiogram.utils.keyboard import ReplyKeyboardBuilder
# @dp.message(Command("reply_builder"))
# async def reply_builder(message: types.Message):
#     builder = ReplyKeyboardBuilder()
#     for i in range(1, 17):
#         builder.add(types.KeyboardButton(text=str(i)))
#     builder.adjust(4)
#     await message.answer("Выберите число:", reply_markup=builder.as_markup(resize_keyboard=True))
