import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
#from constants import *
# Сюда нужно вставить токен, который выдал BotFather
TOKEN = os.getenv('BOT_TOKEN')
bot = telebot.TeleBot(TOKEN)
URL1 = os.getenv('URL1')
URL2 = os.getenv('URL2')
URL3 = os.getenv('URL3')
URL4 = os.getenv('URL4')
URL5 = os.getenv('URL5')
@bot.message_handler(commands=['start'])
def start_command(message):
    # Создаем клавиатуру
    markup = InlineKeyboardMarkup()
    
    # Создаем 5 кнопок. Замените названия и ссылки на свои
    btn1 = InlineKeyboardButton(text="Tribute", url=URL1)
    btn2 = InlineKeyboardButton(text="Stars", url=URL2)
    btn3 = InlineKeyboardButton(text="CryptoClaude", url=URL3)
    btn4 = InlineKeyboardButton(text="Crypto bot", url=URL4)
    btn5 = InlineKeyboardButton(text="TributeWeb", url=URL5)
    
    # Добавляем кнопки в клавиатуру
    # В данном случае каждая кнопка будет на новой строке. 
    # Если хочешь несколько кнопок в один ряд, используй markup.row(btn1, btn2)
    markup.add(btn1)
    markup.add(btn2)
    markup.add(btn3)
    markup.add(btn4)
    markup.add(btn5)
    
    # Отправляем сообщение с прикрепленной клавиатурой
    bot.send_message(
        message.chat.id, 
        "Привет! При оплате с помощью Tribute действует пробный период. Нажми на любую из кнопок ниже, чтобы оплатить с помощью:", 
        reply_markup=markup
    )

# Запускаем бота, чтобы он работал непрерывно
if __name__ == '__main__':
    print("Бот запущен...")
    bot.polling(none_stop=True)
