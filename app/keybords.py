from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder, ReplyKeyboardBuilder

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

# инлайн клавиатура
inline_main = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text='Каталог', callback_data='catalog'),
        InlineKeyboardButton(text='Корзина', callback_data='cart'),
    ],
    [
        InlineKeyboardButton(text='Контакты', callback_data='contacts')
    ]
])

catalog = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text='Nike', callback_data='item_nike'),
        InlineKeyboardButton(text='Adidas', callback_data='item_adidas'),
    ],
    [
        InlineKeyboardButton(text='Rebook', callback_data='item_rebook')
    ]
])

back = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text='Назад', callback_data='catalog')
    ]
])



async def catalog_builder():
    brands = ['Nike', 'Adidas', 'Puma', 'Rebook', 'NewBalans', 'UnderArmour']
    keyboard = InlineKeyboardBuilder()
    for br in brands:
        keyboard.add(InlineKeyboardButton(text=br, callback_data=f'item_{br}'))
    keyboard.add(InlineKeyboardButton(text='Назад', callback_data='menu'))
    return keyboard.adjust(2).as_markup()

async def menu_builder():
    keys = ['Каталог', 'Корзина', 'Контакты']
    keyboard1 = ReplyKeyboardBuilder()
    for key in keys:
        keyboard1.add(KeyboardButton(text=key))
    return keyboard1.adjust(2).as_markup()