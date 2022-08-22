import telebot
from telebot import types
import requests


bot = telebot.TeleBot(token='5488188309:AAGdujULs7Q-X6xaRskQ73_GU1hCkHhH7_k')


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Привет, Бот!")
    markup.add(btn1)
    bot.send_message(message.from_user.id, text="Привет! Я погодный бот"
                     .format(message.from_user), reply_markup=markup)


@bot.message_handler(commands=['info'])
def info(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Понятно!")
    markup.add(btn1)
    bot.send_message(message.from_user.id, f"Умею показывать погоду в разных городах. Необходимо вводить полное название"
                                           f" города, инача он не определится!", reply_markup=markup)


@bot.message_handler(content_types=['text'])
def weather_bot(message):
    if message.text == "Привет, Бот!":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Покажи погоду в Ростове")
        btn2 = types.KeyboardButton("Покажи погоду в Москве")
        btn3 = types.KeyboardButton("Выбрать город")
        markup.add(btn1, btn2, btn3)
        bot.send_message(message.from_user.id, f"Выберите действие", reply_markup=markup)
    elif message.text == "Покажи погоду в Ростове":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Покажи погоду в Ростове")
        btn2 = types.KeyboardButton("Покажи погоду в Москве")
        btn3 = types.KeyboardButton("Выбрать город")
        markup.add(btn1, btn2, btn3)
        response = requests.get('https://www.wttr.in/Ростов-на-Дону?0T&lang=ru')
        bot.send_message(message.from_user.id, f"{response.text}", reply_markup=markup)
    elif message.text == "Покажи погоду в Москве":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Покажи погоду в Ростове")
        btn2 = types.KeyboardButton("Покажи погоду в Москве")
        btn3 = types.KeyboardButton("Выбрать город")
        markup.add(btn1, btn2, btn3)
        response = requests.get('https://www.wttr.in/Москва?0T&lang=ru')
        bot.send_message(message.from_user.id, f"{response.text}", reply_markup=markup)
    elif message.text == "Выбрать город":
        mesg = bot.send_message(message.from_user.id, f"Введите название города (водить нужно полное название, иначе "
                                                      f"город не отпеределится)")
        bot.register_next_step_handler(mesg, choice_city)
    else:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Покажи погоду в Ростове")
        btn2 = types.KeyboardButton("Покажи погоду в Москве")
        btn3 = types.KeyboardButton("Выбрать город")
        markup.add(btn1, btn2, btn3)
        bot.send_message(message.from_user.id, f"Могу показывать погоду в разных городах", reply_markup=markup)


def choice_city(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Покажи погоду в Ростове")
    btn2 = types.KeyboardButton("Выбрать город")
    markup.add(btn1, btn2)
    response = requests.get(f'https://www.wttr.in/{message.text}?0T&lang=ru')
    bot.send_message(message.from_user.id, f"Вы выбрали {response.text}", reply_markup=markup)


bot.polling(none_stop=True, interval=0)
