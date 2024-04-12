import telebot
import requests
from telebot import types

token = ''

API = ''

bot = telebot.Teleot(token)

@bot.message_handler(commands=['start'])
def start(message):
    user_info = get_info(message)
    store_user_data(message.chat.id, user_info)
    markup=types.InlineKeyboardMarkup()
    markup.row(types.InlineKeyboardButton('GBP', callback_data='GBP'),
               types.InlineKeyboardButton('USD', callback_data='USD'),
               types.InlineKeyboardButton('RUB', callback_data='RUB'))
    bot.send_message(message.chat.id, "Choose a currency:", reply_markup = markup)
