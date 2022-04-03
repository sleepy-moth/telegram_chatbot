
import telebot
import DaTa # Класс с данными юзера
import Confid # Хранение Токена(config)
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

bot = telebot.TeleBot(Confid.TOKEN, parse_mode=None)
bot_aio = Bot(token=Confid.TOKEN)
dp = Dispatcher(bot_aio)


@bot.message_handler(commands=['start']) #Начальное приветствие
def start_message(message):
    bot.send_message(message.from_user.id,"Здаров, зарегистрируйся по братски")
    bot.send_message(message.from_user.id, "Введите логин")  # Запрос Логина

    @bot.message_handler()
    def name_login(message: types.Message):
        DaTa.login = message.text
        bot.send_message(message.from_user.id,
                            "Твой логин {}? Ладно".format(DaTa.login)) # Подтверждение логина и ввод в перменную класса DaTa
        bot.send_message(message.from_user.id, "Введите пароль") # Запрос пароля
    @bot.message_handler()
    def name_password(message: types.Message):
        DaTa.password = message.text
        bot.send_message(message.from_user.id,
                             "Значит твой пароль {}?".format(DaTa.password)) #Ввод пароля и перенос в переменную класса DaTa

bot.polling(none_stop=True, interval=0)
