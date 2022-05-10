from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

button=ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Rasmdagi matnni o'zbek tiliga tarjima qilish")
        ],
        [
            KeyboardButton(text="Texni o'zbek tiliga tarjima qilish")
        ],
[
            KeyboardButton(text="Texni auidoga ogirish")
        ],
    ],
    resize_keyboard=True
)