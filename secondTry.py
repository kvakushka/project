import telebot
import os
import time

bot = telebot.TeleBot('947227617:AAEBlhomRlRuqeTymeM-zVo9Pn6JmxwgVf4')

keyboard = telebot.types.ReplyKeyboardMarkup()
keyboard.row('Привет', 'Пока', 'ты лох?', 'песенка', 'музыка')

keyboard_choice = telebot.types.ReplyKeyboardMarkup()
keyboard_choice.row('Christmas mood', 'In love', 'Gym', 'Sad', 'Party', 'Childhood', 'For studying', 'Поныть', 'Стихи',
                    'Меланхолия')
keyboard_menu = telebot.types.ReplyKeyboardMarkup()
keyboard_menu.row('По настроению', 'По жанрам', 'По дате рождения', 'Топ песен', 'Для сна', 'Акустика')

keyboard_genre = telebot.types.ReplyKeyboardMarkup()
keyboard_genre.row('Поп', 'Алтернатива', 'Рок', 'R&B', 'Электроника', 'Инди', 'Блюз-рок')

Christmas_id = ['CQADAgADfgUAAkn8yEuQTb7jsefMwRYE', 'CQADAgADuQMAAlB-0Esk5DfJL3PL3xYE', 'CQADAgADugMAAlB-0EsKKBL745odthYE',
             'CQADAgADiAUAAlHpyEtHo19BOckZBhYE', 'CQADAgADigUAAlHpyEsncQwqd_wN-hYE', 'CQADAgADEgUAAuKn0Evq-j1RUa4aERYE',
             'CQADAgADDgYAAkn80EtWBclWfG6KhhYE', 'CQADAgADDwYAAkn80Evvwca7YbFaoBYE', 'CQADAgADEAYAAkn80Euh1lFcu-MJNBYE']

InLove_id = ['CQADAgADJgQAAlB-0Es96dEgDKGQghYE', 'CQADAgADGQYAAkn80EvnNZ9FNewtwxYE', 'CQADAgADGwYAAkn80EuN3DNk4QMXhxYE',
          'CQADAgADFgUAAuKn0Etzpel0EkiqURYE', 'CQADAgADGgUAAuKn0EsBD2q95fkLaRYE', 'CQADAgADIwYAAkn80Ev1DMxu78JQXhYE',
          'CQADAgADJAYAAkn80EsnID9m4-LQDRYE', 'CQADAgADJgYAAkn80EuDlBByM1LzphYE', 'CQADAgADJwYAAkn80Et4CCNhik8t4RYE',
          'CQADAgADKAYAAkn80Eshm3ICw0V4kxYE', 'CQADAgADHwUAAuKn0EvxUqwOz4SkVRYE', 'CQADAgADKQYAAkn80EtATnQVRpPWhxYE',
          'CQADAgADKgYAAkn80EuSp890BjtcnhYE', 'CQADAgADKwYAAkn80Ev_cdb_6Ylm4RYE', 'CQADAgADLAYAAkn80EtAhTYEUxHk0xYE',
          'CQADAgADJAUAAuKn0EsOjFP7zHSMGxYE', 'CQADAgADJQUAAuKn0EvNjca2H-iMVxYE', 'CQADAgADLQYAAkn80EsmWwg4rNxR8xYE',
          'CQADAgADJwUAAuKn0EuH_xVjSLMGERYE', 'CQADAgADLwYAAkn80EtQPbwwElckAAEWBA', 'CQADAgADKQQAAlB-0Etro6O-CxIXqhYE']

# Сделать листы для остальных песен
@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет, хочешь поговорить?', reply_markup=keyboard)


@bot.message_handler(commands=['song'])
def find_file_ids(message):
    for file in os.listdir('/Users/elinaaptineeva/Desktop/music_bot/in.love/'):
        if file.split('.')[-1] == 'm4a' or 'mp3':
            songg = open('/Users/elinaaptineeva/Desktop/music_bot/in.love/'+file, 'rb')
            msg = bot.send_audio(message.chat.id, songg, None)
            # А теперь отправим вслед за файлом его file_id
            bot.send_message(message.chat.id, msg.audio.file_id, reply_to_message_id=msg.message_id)
        time.sleep(20)  #найти оптимальное время



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


