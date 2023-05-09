from aiogram import Bot, Dispatcher, types, executor
import buttons as bt
import json
import colorama
import random
from colorama import Fore, Style
colorama.init(autoreset=True)

open = open('token.json', 'r')
config = json.load(open)
bot = Bot(config['token'])
dp = Dispatcher(bot)





user_name = "user"

@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.answer("Привет! Как тебя зовут?")
    @dp.message_handler()
    async def input_name(message: types.Message):
        global user_name
        user_name = message.text
        await message.answer(f"Приятно познакомиться {user_name}!", reply_markup=bt.start_menu)




@dp.message_handler(text="Выбор")
async def choose(message: types.Message):
    text = message.text
    if text.startswith('Выбор'):
            await bot.delete_message(chat_id=message.chat.id, message_id=message.message_id)
    await bot.send_message(chat_id = message.from_user.id, text=f"{user_name} выбери интересующее тебя приложение", reply_markup=bt.choose_tools)
    @dp.callback_query_handler(text="getnumber")
    async def choose_random(message: types.Message):
        await bot.send_message(chat_id = message.from_user.id, text=f"Мне нужно понять от скольки до скольки выдать вам число")
        await bot.send_message(chat_id = message.from_user.id, text=f"Введите первое число")
        global first_random
        global second_random
        first_random = None
        second_random = None

        @dp.message_handler()
        async def handle_numbers(message: types.Message):
            await bot.delete_message(chat_id=message.chat.id, message_id=message.message_id)
            global first_random
            global second_random
            if not first_random:
                first_random = message.text
                await message.answer(text=f"Введите второе число")
            elif not second_random:
                second_random = message.text
                await message.answer(text=f"число от {first_random} до {second_random} : ")
                random_number = random.randint(int(first_random), int(second_random))
                await message.answer(text=f"⚪️{random_number}⚪️", reply_markup=bt.randomizer_again_menu)
                await message.answer(text=f"{user_name} выбери интересующее тебя приложение", reply_markup=bt.choose_tools)
                
            else:
                await message.answer(text=f'Вы уже ввели два числа. Поэтому нажмите "Рандомайзер" ещё раз')
    @dp.callback_query_handler(text="getweatherinfo")
    async def getweather(message: types.Message):
        await bot.send_message(chat_id = message.from_user.id, text=f"В разработке...")
    @dp.callback_query_handler(text="convert_money")
    async def getweather(message: types.Message):
        await bot.send_message(chat_id = message.from_user.id, text=f"В разработке...")
    @dp.callback_query_handler(text="notice")
    async def getweather(message: types.Message):
        await bot.send_message(chat_id = message.from_user.id, text=f"В разработке...")
    @dp.callback_query_handler(text="soon")
    async def getweather(message: types.Message):
        await bot.send_message(chat_id = message.from_user.id, text=f"Предложите свои идеи для бота @qwoe1x")




    
    









@dp.message_handler(text="Поддержка")
async def choose(message: types.Message):
    await message.answer(text="❤️Спасибо за тестирование❤️",reply_markup=bt.links)

print(Fore.BLUE + Style.BRIGHT + "Слава " + Fore.YELLOW + Style.BRIGHT + "Україні!")
print("\n" * 5)
print(Fore.BLUE + "###################################################")
print(Fore.BLUE + "###################################################")
print(Fore.BLUE + "###################################################")
print(Fore.YELLOW + "###################################################")
print(Fore.YELLOW + "###################################################")
print(Fore.YELLOW + "###################################################")
print('\n' * 14)

if __name__ == "__main__":
    executor.start_polling(dispatcher=dp, skip_updates=True)