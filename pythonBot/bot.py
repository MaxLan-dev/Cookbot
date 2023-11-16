
import telebot

#from utils import get_daily_horoscope


bot = telebot.TeleBot("6619295811:AAHobjQDD1uLuRMhNS6CeeMZtrfJs4ZRPt4")


@bot.message_handler(commands=['start', 'hello'])
def send_welcome(message):
    bot.reply_to(message, "Howdy, how are you doing?")

#
bot.infinity_polling()