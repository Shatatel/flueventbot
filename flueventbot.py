#hello world bot flueventbot

import telebot

bot = telebot.TeleBot("518602976:AAHh0Mosj2RDdxpEBhh6VcFSfOohL6yKmTI")

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Howdy, how are you doing?")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
	bot.reply_to(message, message.text)

bot.polling()
