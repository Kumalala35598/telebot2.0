import config
import telebot
import config
import telebot
from pycbrf import ExchangeRates
from datetime import date
from telebot import types

today = date.today()

rates = ExchangeRates(today)
bot = telebot.TeleBot(config.TOKEN)
#Создаем клавиатуру
menu = types.ReplyKeyboardMarkup( resize_keyboard=True)
#Создаем кнопку
btnKZT = types.KeyboardButton(text="🇰🇿 Казахстанский тенге  ")
btnUSD = types.KeyboardButton(text="🇺🇸 Доллар США")
btnEUR = types.KeyboardButton(text="🇪🇺 Евро")
btnCHF = types.KeyboardButton(text="🇨🇭 Швейцарский франк")
btnCNY = types.KeyboardButton(text="🇨🇳 Китайский юань")
#добавляем кнопку на клавиатуру
menu.add(btnUSD, btnEUR)
menu.add(btnCHF, btnKZT)
menu.add(btnCNY)
@bot.message_handler(commands=["start"])
def start(message):
	#reply_markup=menu - прикрепляем клавиатуру к сообщению
	bot.send_message(message.chat.id, "Выбери валюту:", reply_markup=menu)
#делаем реакцию на кнопку
@bot.message_handler(func = lambda message: message.text=='🇺🇸 Доллар США')
def usd(message):
	text = "1 Доллар США ="+str(rates['USD'].rate)+"руб."
	bot.send_message(message.chat.id, text)
@bot.message_handler(func = lambda message: message.text=='🇪🇺 Евро')
def eur(message):
	text = "1 Евро ="+str(rates['EUR'].rate)+"руб."
	bot.send_message(message.chat.id, text)
@bot.message_handler(func = lambda message: message.text=='🇰🇿 Казахстанский тенге')
def kzt(message):
	text = "1 Казахстанский тенге ="+str(rates['KZT'].rate)+"руб."
	bot.send_message(message.chat.id, text)
@bot.message_handler(func = lambda message: message.text=='🇨🇭 Швейцарский франк')
def eur(message):
	text = "1 Швейцарский франк ="+str(rates['CHF'].rate)+"руб."
	bot.send_message(message.chat.id, text)
@bot.message_handler(func = lambda message: message.text=='🇨🇳 Китайский юань')
def kzt(message):
	text = "1 Китайский юань ="+str(rates['CNY'].rate)+"руб."
	bot.send_message(message.chat.id, text)

if __name__ == '__main__':
	bot.infinity_polling()