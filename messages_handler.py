import telebot
from message_reply import message_reply


def response(bot, message):
    input_text = message.text.lower()
    user_name = message.from_user.first_name
    reply_text = message_reply(input_text, user_name)
    bot.reply_to(message, reply_text)
