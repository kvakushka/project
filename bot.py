import telebot

bot = telebot.TeleBot('947227617:AAEBlhomRlRuqeTymeM-zVo9Pn6JmxwgVf4')
keyboard = telebot.types.ReplyKeyboardMarkup()
keyboard.row('Привет', 'Пока', 'ты лох?', 'Я тебя люблю')

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет, хочешь поговорить?', reply_markup=keyboard)


@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text.lower() == 'привет':
        bot.send_message(message.chat.id, 'Приветос')
    elif message.text.lower() == 'пока':
        bot.send_message(message.chat.id, 'Прощай......я буду скучать')
    elif message.text.lower() == 'ты лох?':
        bot.send_message(message.chat.id, 'сам ты лох, дебил')
    elif message.text.lower() == 'я тебя люблю':
        bot.send_message(message.chat.id, 'А я тебя нет. Убейся')
    elif message.text.lower() == 'да':
        bot.send_message(message.chat.id, 'Че, у тебя совсем друзей нет?')

bot.polling(none_stop = True, interval = 0)
