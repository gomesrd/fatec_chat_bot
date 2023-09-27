import telebot
from config import KEY_API
from messages_handler import response

bot = telebot.TeleBot(KEY_API)


@bot.message_handler()
def handle_message(message):
    response(bot, message)


print("Servidor Ativo!")
bot.polling()
