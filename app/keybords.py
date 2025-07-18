from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder


# reply клавиатура
main = ReplyKeyboardMarkup(keyboard=[
        [
            KeyboardButton(text='Каталог'),
            KeyboardButton(text='Корзина'),
        ],
        [
            KeyboardButton(text='Контакты'),
        ]
    ],
    resize_keyboard=True,
    input_field_placeholder='Выберите пункт ниже'
)

async def catalog_builder():
    brands = ['Nike', 'Adidas', 'Puma', 'Rebook', 'New Balans', 'Under Armour']
    keyboard = InlineKeyboardBuilder()
    for br in brands:
        keyboard.add(InlineKeyboardButton(text=br, callback_data=f'item_{br}'))
    keyboard.add(InlineKeyboardButton(text='Назад', callback_data='menu'))
    return keyboard.adjust(2).as_markup()
