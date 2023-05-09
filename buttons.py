from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup
start_menu = ReplyKeyboardMarkup(resize_keyboard=True)
support = KeyboardButton("Поддержка")
choose_menu = KeyboardButton("Выбор")
cancel = KeyboardButton("Назад")
start_menu.add(choose_menu, support)


choose_tools = InlineKeyboardMarkup(row_width=3)
randomizer = InlineKeyboardButton(text="Рандомайзер", callback_data="getnumber")
randomizer_again = InlineKeyboardButton(text="Повторить", callback_data="getnumber")
randomizer_again_menu = InlineKeyboardMarkup(row_width=2)
randomizer_again_menu.add(randomizer_again)
weather = InlineKeyboardButton(text="Погода", callback_data="getweatherinfo")
money_convert = InlineKeyboardButton(text="Конвертер валют", callback_data="convert_money")
notice = InlineKeyboardButton(text="Напоминание", callback_data="notice")
soon = InlineKeyboardButton(text="Soon...", callback_data="soon")
choose_tools.add(randomizer, weather, money_convert, notice, soon)



links = InlineKeyboardMarkup(row_width=2)
tg = InlineKeyboardButton("Тг для связи", url="https://t.me/qwoe1x")
git = InlineKeyboardButton("Code", url="https://github.com/qwoe1x/tgtools")
links.add(tg, git)