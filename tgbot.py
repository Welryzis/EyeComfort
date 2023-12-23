import telebot
import config


def send_message(message: str = config.TG_MESSAGE):
    bot = telebot.TeleBot(config.TG_BOT_TOKEN)
    bot.send_message(config.TG_CHAT_ID, message)
