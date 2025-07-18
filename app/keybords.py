from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

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
