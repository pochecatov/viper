import telebot
from telebot import types
import random;


token =""
bot =telebot.TeleBot(token)
image ='files'


pochekutov =[    
     ('files/picture.jpg', ('<blockquote>Мы про взрывы, про пожары\n Сочинили ноту ТАСС…\n Но примчались санитары\n И зафиксировали нас.</blockquote>')),
   
]


@bot.message_handler(commands=['start'])
def start_message(message):
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    button = types.KeyboardButton('Хочу случайную картинку')
    keyboard.add(button)
    
    bot.send_message(
        message.chat.id,
        "Привет",
        reply_markup=keyboard
    )

@bot.message_handler(func=lambda message: message.text == 'Хочу случайную картинку')
def send_pochekutov(message):
    img, text = random.choice(pochekutov)
    try:
        with open(img, 'rb') as photo:
            bot.send_photo(message.chat.id, photo, caption=text,parse_mode='HTML')
    except FileNotFoundError:
        bot.send_message(message.chat.id, f"Ошибка: Файл {img} не найден.")
    except Exception as e:
        bot.send_message(message.chat.id, f"Произошла ошибка: {e}")

if __name__ == '__main__':
  
    bot.polling(none_stop=True)
