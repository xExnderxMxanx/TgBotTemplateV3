from aiogram.types.keyboard_button   import InlineKeyboardMarkup
from aiogram.types.inline_keyboard_button import InlineKeyboardButton

class Keyboard(object):
    def __init__(self, id_orLang: str | int) -> None:
        super(Keyboard, self).__init__()