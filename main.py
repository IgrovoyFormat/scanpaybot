import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
import os

TOKEN = os.getenv('BOT_TOKEN')
bot = telebot.TeleBot(TOKEN)

URL1 = os.getenv('URL1')
URL2 = os.getenv('URL2')
URL3 = os.getenv('URL3')

@bot.message_handler(commands=['start'])
def start_command(message):
    markup = InlineKeyboardMarkup()
    
    btn1 = InlineKeyboardButton(text="Tribute", url=URL1)
    btn2 = InlineKeyboardButton(text="Crypto bot", url=URL2)
    btn3 = InlineKeyboardButton(text="Support", url=URL3)
    
    markup.add(btn1)
    markup.add(btn2)
    markup.add(btn3)
    
    bot.send_message(
        message.chat.id, 
        "Hi! 👋 I'm your personal payment assistant.", 
        reply_markup=markup
    )

if __name__ == '__main__':
    print("Бот запущен...")
    bot.polling(none_stop=True)

