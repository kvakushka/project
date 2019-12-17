import telebot

import os
import time




bot = telebot.TeleBot('947227617:AAEBlhomRlRuqeTymeM-zVo9Pn6JmxwgVf4')
keyboard = telebot.types.ReplyKeyboardMarkup()
keyboard.row('Привет', 'Пока', 'песенка', 'музыка')

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет, хочешь поговорить?', reply_markup=keyboard)

@bot.message_handler(commands=['song'])
def find_file_ids(message):
    for file in os.listdir('/Users/elinaaptineeva/Desktop/music/'):
        if file.split('.')[-1] == 'm4a' or 'mp3':
            songg = open('/Users/elinaaptineeva/Desktop/music/'+file, 'rb')
            msg = bot.send_audio(message.chat.id, songg, None)
            # А теперь отправим вслед за файлом его file_id
            bot.send_message(message.chat.id, msg.audio.file_id, reply_to_message_id=msg.message_id)
        time.sleep(1)

keyboard_choice = telebot.types.ReplyKeyboardMarkup()
keyboard_choice.row('Christmas mood', 'In love', 'Gym', 'Sad', 'Party', 'Childhood', 'For studying', 'Поныть', 'Стихи',
                    'Меланхолия')



@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text.lower() == 'привет':
        bot.send_message(message.chat.id, 'Приветос')
    elif message.text.lower() == 'пока':
        bot.send_message(message.chat.id, 'Прощай......я буду скучать')
    elif message.text.lower() == 'ты лох?':
        bot.send_message(message.chat.id, 'сам ты лох, дебил')
    elif message.text.lower() == 'песенка':
        bot.send_audio(message.chat.id, 'CQADAgADSQUAAkn8yEunFhTlnfi6khYE')
    elif message.text.lower() == 'музыка':
        bot.send_message(message.chat.id, 'Какое у тебя сейчас настроение?', reply_markup=keyboard_choice) #нужно найти инфу о нормальном расположении прямоугольничков
    else:
        bot.send_sticker(message.chat.id, 'CAADAgADNAADkp8eEfIdTHZlMTXQFgQ')



bot.polling(none_stop = True, interval = 0)


