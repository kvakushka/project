import telebot
import os
import time
import random

bot = telebot.TeleBot('947227617:AAEBlhomRlRuqeTymeM-zVo9Pn6JmxwgVf4')

#keyboard = telebot.types.ReplyKeyboardMarkup()
#keyboard.row('Привет', 'Пока', 'ты лох?', 'песенка', 'музыка')

keyboard_mood = telebot.types.ReplyKeyboardMarkup()
keyboard_mood.row('New Year', 'In love', 'Gym', 'Sad')
keyboard_mood.row('Party', 'Nostalgia', 'Studying')
keyboard_mood.row('Poetry', 'Melancholy', 'Назад')

keyboard_menu = telebot.types.ReplyKeyboardMarkup()
keyboard_menu.row('По настроению', 'По жанрам')
keyboard_menu.row('По дате рождения', 'Топ песен')
keyboard_menu.row('Для сна', 'Акустика')

keyboard_genre = telebot.types.ReplyKeyboardMarkup()
keyboard_genre.row('Pop', 'Альтернатива')
keyboard_genre.row('Рок', 'R&B', 'Электроника')
keyboard_genre.row('Инди', 'Блюз-рок', 'Назад')

NewYear_id = ['CQADAgADfgUAAkn8yEuQTb7jsefMwRYE', 'CQADAgADuQMAAlB-0Esk5DfJL3PL3xYE', 'CQADAgADugMAAlB-0EsKKBL745odthYE',
             'CQADAgADiAUAAlHpyEtHo19BOckZBhYE', 'CQADAgADigUAAlHpyEsncQwqd_wN-hYE', 'CQADAgADEgUAAuKn0Evq-j1RUa4aERYE',
             'CQADAgADDgYAAkn80EtWBclWfG6KhhYE', 'CQADAgADDwYAAkn80Evvwca7YbFaoBYE', 'CQADAgADEAYAAkn80Euh1lFcu-MJNBYE',
             'CQADAgADzwYAAkn80Etwrhhg48UHVhYE', 'CQADAgAD0AYAAkn80EsKVrpSlJGvPhYE', 'CQADAgADWwQAAuKn2Evvw1mMqBEBZBYE']

InLove_id = ['CQADAgADJgQAAlB-0Es96dEgDKGQghYE', 'CQADAgADGQYAAkn80EvnNZ9FNewtwxYE', 'CQADAgADGwYAAkn80EuN3DNk4QMXhxYE',
          'CQADAgADFgUAAuKn0Etzpel0EkiqURYE', 'CQADAgADGgUAAuKn0EsBD2q95fkLaRYE', 'CQADAgADIwYAAkn80Ev1DMxu78JQXhYE',
          'CQADAgADJAYAAkn80EsnID9m4-LQDRYE', 'CQADAgADJgYAAkn80EuDlBByM1LzphYE', 'CQADAgADJwYAAkn80Et4CCNhik8t4RYE',
          'CQADAgADKAYAAkn80Eshm3ICw0V4kxYE', 'CQADAgADHwUAAuKn0EvxUqwOz4SkVRYE', 'CQADAgADKQYAAkn80EtATnQVRpPWhxYE',
          'CQADAgADKgYAAkn80EuSp890BjtcnhYE', 'CQADAgADKwYAAkn80Ev_cdb_6Ylm4RYE', 'CQADAgADLAYAAkn80EtAhTYEUxHk0xYE',
          'CQADAgADJAUAAuKn0EsOjFP7zHSMGxYE', 'CQADAgADJQUAAuKn0EvNjca2H-iMVxYE', 'CQADAgADLQYAAkn80EsmWwg4rNxR8xYE',
          'CQADAgADJwUAAuKn0EuH_xVjSLMGERYE', 'CQADAgADLwYAAkn80EtQPbwwElckAAEWBA', 'CQADAgADKQQAAlB-0Etro6O-CxIXqhYE']

Gym_id = ['CQADAgADaAQAAuKn2Ev6bqsxt0Z9LhYE', 'CQADAgADaQQAAuKn2EvKeDre7P00wRYE', 'CQADAgADagQAAuKn2EsNZKbj2w55FxYE',
          'CQADAgAD2QYAAkn80EvOWq-vhPwrnRYE', 'CQADAgADbgQAAuKn2EspMN9EhoWJUxYE', 'CQADAgAD2wYAAkn80Et8mVrPnEoyyBYE',
          'CQADAgADcQQAAuKn2EvxxDRi1xLq-xYE', 'CQADAgADhAQAAl_02UsxEX7mDgRL5RYE', 'CQADAgAD3AYAAkn80EvGTNAY4KErPBYE',
          'CQADAgAD3QYAAkn80EvQ13Zk_o8HaRYE', 'CQADAgADdQQAAuKn2EtDf6wHikeXvxYE', 'CQADAgADdgQAAuKn2EslNtgy_6fp0RYE',
          'CQADAgADeAQAAuKn2Etqv6ihz5LMXRYE', 'CQADAgADegQAAuKn2EtRt-NRDpb5XxYE', 'CQADAgADhgQAAl_02Ut1DFAy6WP96RYE',
          'CQADAgAD4AYAAkn80EusWEgzGgVX2xYE']

Sad_id =[]

Party_id = []

Nostalgia_id = []

Studying_id =[]

Poetry_id = []

Melancholy_id = []



# Сделать листы для остальных песен

#new_list = random.sample(Christmas_id, k=5)
#def random_songs():
    #for i in range(len(new_list)):     В таком случае в ответе бота будут new_list[0] и тд
        #return new_list[i]



@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет, как ты хочешь осуществить выбор музыки?', reply_markup=keyboard_menu)


@bot.message_handler(commands=['song'])
def find_file_ids(message):
    for file in os.listdir('/Users/elinaaptineeva/Desktop/gym/'):
        if file.split('.')[-1] == 'm4a' or 'mp3':
            songg = open('/Users/elinaaptineeva/Desktop/gym/'+file, 'rb')
            msg = bot.send_audio(message.chat.id, songg, None)
            bot.send_message(message.chat.id, msg.audio.file_id, reply_to_message_id=msg.message_id)
        time.sleep(30)


@bot.message_handler(func=lambda message: True, content_types=['text']) #Все в одной функции, так как все сообщения имеют один тип text
def send_text(message):
    if message.text.lower() == 'привет':
        bot.send_message(message.chat.id, 'Приветос')
    elif message.text.lower() == 'пока':
        bot.send_message(message.chat.id, 'Прощай......я буду скучать')
    elif message.text.lower() == 'назад':
        bot.send_message(message.chat.id, 'Как ты хочешь осуществить выбор музыки?', reply_markup=keyboard_menu)

        #Выбор для настроения
    elif message.text.lower() == 'по настроению':
        bot.send_message(message.chat.id, 'Какое у тебя настроение?', reply_markup=keyboard_mood)
    elif message.text.lower() == 'new year':
        bot.send_audio(message.chat.id, random.choice(NewYear_id), disable_notification=1)
        bot.send_audio(message.chat.id, random.choice(NewYear_id), disable_notification=1)
        bot.send_audio(message.chat.id, random.choice(NewYear_id), disable_notification=1)
        bot.send_audio(message.chat.id, random.choice(NewYear_id), disable_notification=1)
        bot.send_audio(message.chat.id, random.choice(NewYear_id), disable_notification=1)
        bot.send_sticker(message.chat.id, 'CAADAgADEAADkp8eEQXW_GnuhWb_FgQ')

    elif message.text.lower() == 'in love':
        bot.send_audio(message.chat.id, random.choice(InLove_id), disable_notification=1)
        bot.send_audio(message.chat.id, random.choice(InLove_id), disable_notification=1)
        bot.send_audio(message.chat.id, random.choice(InLove_id), disable_notification=1)
        bot.send_audio(message.chat.id, random.choice(InLove_id), disable_notification=1)
        bot.send_audio(message.chat.id, random.choice(InLove_id), disable_notification=1)

    elif message.text.lower() == 'gym':
        bot.send_audio(message.chat.id, random.choice(Gym_id), disable_notification=1)
        bot.send_audio(message.chat.id, random.choice(Gym_id), disable_notification=1)
        bot.send_audio(message.chat.id, random.choice(Gym_id), disable_notification=1)
        bot.send_audio(message.chat.id, random.choice(Gym_id), disable_notification=1)
        bot.send_audio(message.chat.id, random.choice(Gym_id), disable_notification=1)
        bot.send_sticker(message.chat.id, 'CAADAgADXgADaUCAC_ik5ou43wUkFgQ')

    elif message.text.lower() == 'sad':
        bot.send_audio(message.chat.id, random.choice(), disable_notification=1)
        bot.send_audio(message.chat.id, random.choice(), disable_notification=1)
        bot.send_audio(message.chat.id, random.choice(), disable_notification=1)
        bot.send_audio(message.chat.id, random.choice(), disable_notification=1)
        bot.send_audio(message.chat.id, random.choice(), disable_notification=1)
        bot.send_sticker(message.chat.id, '')

    elif message.text.lower() == 'party':
        bot.send_audio(message.chat.id, random.choice(), disable_notification=1)
        bot.send_audio(message.chat.id, random.choice(), disable_notification=1)
        bot.send_audio(message.chat.id, random.choice(), disable_notification=1)
        bot.send_audio(message.chat.id, random.choice(), disable_notification=1)
        bot.send_audio(message.chat.id, random.choice(), disable_notification=1)
        bot.send_sticker(message.chat.id, '')

    elif message.text.lower() == 'nostalgia':
        bot.send_audio(message.chat.id, random.choice(), disable_notification=1)
        bot.send_audio(message.chat.id, random.choice(), disable_notification=1)
        bot.send_audio(message.chat.id, random.choice(), disable_notification=1)
        bot.send_audio(message.chat.id, random.choice(), disable_notification=1)
        bot.send_audio(message.chat.id, random.choice(), disable_notification=1)
        bot.send_sticker(message.chat.id, '')

    elif message.text.lower() == 'studying':
        bot.send_audio(message.chat.id, random.choice(), disable_notification=1)
        bot.send_audio(message.chat.id, random.choice(), disable_notification=1)
        bot.send_audio(message.chat.id, random.choice(), disable_notification=1)
        bot.send_audio(message.chat.id, random.choice(), disable_notification=1)
        bot.send_audio(message.chat.id, random.choice(), disable_notification=1)
        bot.send_sticker(message.chat.id, '')

    elif message.text.lower() == 'poetry':
        bot.send_audio(message.chat.id, random.choice(), disable_notification=1)
        bot.send_audio(message.chat.id, random.choice(), disable_notification=1)
        bot.send_audio(message.chat.id, random.choice(), disable_notification=1)
        bot.send_audio(message.chat.id, random.choice(), disable_notification=1)
        bot.send_audio(message.chat.id, random.choice(), disable_notification=1)
        bot.send_sticker(message.chat.id, '')

    elif message.text.lower() == 'melancholy':
        bot.send_audio(message.chat.id, random.choice(), disable_notification=1)
        bot.send_audio(message.chat.id, random.choice(), disable_notification=1)
        bot.send_audio(message.chat.id, random.choice(), disable_notification=1)
        bot.send_audio(message.chat.id, random.choice(), disable_notification=1)
        bot.send_audio(message.chat.id, random.choice(), disable_notification=1)
        bot.send_sticker(message.chat.id, '')
        
        #Выбор для жанра
        
    else:
        bot.send_sticker(message.chat.id, 'CAADAgADNAADkp8eEfIdTHZlMTXQFgQ')


bot.polling(none_stop = True, interval = 0)


