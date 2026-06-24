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
    btn2 = InlineKeyboardButton(text="Stars", url=URL2)
    btn3 = InlineKeyboardButton(text="Support", url=URL3)
    
    markup.add(btn1)
    markup.add(btn2)
    
    bot.send_message(
        message.chat.id, 
        "Привет! При оплате с помощью Tribute действует пробный период. Нажми на любую из кнопок ниже, чтобы оплатить с помощью:", 
        reply_markup=markup
    )

if __name__ == '__main__':
    print("Бот запущен...")
    bot.polling(none_stop=True)

