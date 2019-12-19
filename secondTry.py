import telebot
import os
import time
import random
import openpyxl

bot = telebot.TeleBot('947227617:AAEBlhomRlRuqeTymeM-zVo9Pn6JmxwgVf4')

workbook = openpyxl.load_workbook(filename="/Users/elinaaptineeva/Desktop/Music.xlsx")
ny_sheet = workbook["NewYear_id"]
love_sheet = workbook["InLove_id"]
gym_sheet = workbook["Gym_id"]
sad_sheet = workbook["Sad_id"]
party_sheet = workbook["Party_id"]
nostalgia_sheet = workbook["Nostalgia_id"]
studying_sheet = workbook["Studying_id"]
pop_sheet = workbook["Pop_id"]
alternative_sheet = workbook["Alternative_id"]
rock_sheet = workbook["Rock_id"]
randb_sheet = workbook["RandB_id"]
electro_sheet = workbook["Electro_id"]
sleep_sheet = workbook["ForSleep_id"]
acoustics_sheet = workbook["Acoustics_id"]

ny_list = [ny_sheet.cell(row=i,column=1).value for i in range(1,13)]
love_list = [love_sheet.cell(row=i,column=1).value for i in range(1,21)]
gym_list = [gym_sheet.cell(row=i,column=1).value for i in range(1,16)]
sad_list = [sad_sheet.cell(row=i,column=1).value for i in range(1,21)]
party_list = [party_sheet.cell(row=i,column=1).value for i in range(1,19)]
nostalgia_list = [nostalgia_sheet.cell(row=i,column=1).value for i in range(1,12)]
studying_list = [studying_sheet.cell(row=i,column=1).value for i in range(1,10)]
pop_list = [pop_sheet.cell(row=i,column=1).value for i in range(1,16)]
alternative_list = [alternative_sheet.cell(row=i,column=1).value for i in range(1,13)]
rock_list = [rock_sheet.cell(row=i,column=1).value for i in range(1,18)]
randb_list = [randb_sheet.cell(row=i,column=1).value for i in range(1,21)]
electro_list = [electro_sheet.cell(row=i,column=1).value for i in range(1,21)]
sleep_list = [sleep_sheet.cell(row=i,column=1).value for i in range(1,21)]
acoustics_list = [acoustics_sheet.cell(row=i,column=1).value for i in range(1,21)]
#birthday_list = рандом из всех листов
#top просто 5 наших песен


#keyboard = telebot.types.ReplyKeyboardMarkup()
#keyboard.row('Привет', 'Пока', 'ты лох?', 'песенка', 'музыка')

keyboard_mood = telebot.types.ReplyKeyboardMarkup()
keyboard_mood.row('New Year', 'In love', 'Gym')
keyboard_mood.row('Party', 'Nostalgia', 'Studying')
keyboard_mood.row('Poetry', 'Sad', 'Назад')

keyboard_menu = telebot.types.ReplyKeyboardMarkup()
keyboard_menu.row('По настроению', 'По жанрам')
keyboard_menu.row('По дате рождения', 'Топ песен')
keyboard_menu.row('Для сна', 'Акустика')

keyboard_genre = telebot.types.ReplyKeyboardMarkup()
keyboard_genre.row('Pop', 'Альтернатива')
keyboard_genre.row('Рок', 'R&B', 'Электроника')
keyboard_genre.row('Назад')


#new_list = random.sample(Christmas_id, k=5)
#def random_songs():
    #for i in range(len(new_list)):     В таком случае в ответе бота будут new_list[0] и тд
        #return new_list[i]


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет, как ты хочешь осуществить выбор музыки?', reply_markup=keyboard_menu)


@bot.message_handler(commands=['song'])
def find_file_ids(message):
    for file in os.listdir('/Users/elinaaptineeva/Desktop/rock/'):
        if file.split('.')[-1] == 'm4a' or 'mp3':
            songg = open('/Users/elinaaptineeva/Desktop/rock/'+file, 'rb')
            msg = bot.send_audio(message.chat.id, songg, None)
            bot.send_message(message.chat.id, msg.audio.file_id, reply_to_message_id=msg.message_id)
        time.sleep(50)


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
        bot.send_audio(message.chat.id, random.choice(ny_list), disable_notification=1) #не нашли функцию, позволяющюю отправлять несколько аудио в одном сообщении,
        bot.send_audio(message.chat.id, random.choice(ny_list), disable_notification=1) #поэтому приходится пять раз отправлять разные сообщения
        bot.send_audio(message.chat.id, random.choice(ny_list), disable_notification=1)
        bot.send_audio(message.chat.id, random.choice(ny_list), disable_notification=1)
        bot.send_sticker(message.chat.id, 'CAADAgADEAADkp8eEQXW_GnuhWb_FgQ')

    elif message.text.lower() == 'in love':
        bot.send_audio(message.chat.id, random.choice(love_list), disable_notification=1)
        bot.send_audio(message.chat.id, random.choice(love_list), disable_notification=1)
        bot.send_audio(message.chat.id, random.choice(love_list), disable_notification=1)
        bot.send_audio(message.chat.id, random.choice(love_list), disable_notification=1)
        bot.send_audio(message.chat.id, random.choice(love_list), disable_notification=1)
        bot.send_sticker(message.chat.id, 'CAADAgADBAADkp8eEavc7j2rScUkFgQ')

    elif message.text.lower() == 'gym':
        bot.send_audio(message.chat.id, random.choice(gym_list), disable_notification=1)
        bot.send_audio(message.chat.id, random.choice(gym_list), disable_notification=1)
        bot.send_audio(message.chat.id, random.choice(gym_list), disable_notification=1)
        bot.send_audio(message.chat.id, random.choice(gym_list), disable_notification=1)
        bot.send_audio(message.chat.id, random.choice(gym_list), disable_notification=1)
        bot.send_sticker(message.chat.id, 'CAADAgADXgADaUCAC_ik5ou43wUkFgQ')

    elif message.text.lower() == 'sad':
        bot.send_audio(message.chat.id, random.choice(sad_list), disable_notification=1)
        bot.send_audio(message.chat.id, random.choice(sad_list), disable_notification=1)
        bot.send_audio(message.chat.id, random.choice(sad_list), disable_notification=1)
        bot.send_audio(message.chat.id, random.choice(sad_list), disable_notification=1)
        bot.send_audio(message.chat.id, random.choice(sad_list), disable_notification=1)
        bot.send_sticker(message.chat.id, 'CAADAQADoBIAApl_iALzktRqOg9uhhYE')

    elif message.text.lower() == 'party':
        bot.send_audio(message.chat.id, random.choice(party_list), disable_notification=1)
        bot.send_audio(message.chat.id, random.choice(party_list), disable_notification=1)
        bot.send_audio(message.chat.id, random.choice(party_list), disable_notification=1)
        bot.send_audio(message.chat.id, random.choice(party_list), disable_notification=1)
        bot.send_audio(message.chat.id, random.choice(party_list), disable_notification=1)
        bot.send_sticker(message.chat.id, 'CAADAgADowADtvArFPC6O5csMnkcFgQ')

    elif message.text.lower() == 'nostalgia':
        bot.send_audio(message.chat.id, random.choice(nostalgia_list), disable_notification=1)
        bot.send_audio(message.chat.id, random.choice(nostalgia_list), disable_notification=1)
        bot.send_audio(message.chat.id, random.choice(nostalgia_list), disable_notification=1)
        bot.send_audio(message.chat.id, random.choice(nostalgia_list), disable_notification=1)
        #bot.send_sticker(message.chat.id, '')

    elif message.text.lower() == 'studying':
        bot.send_audio(message.chat.id, random.choice(studying_list), disable_notification=1)
        bot.send_audio(message.chat.id, random.choice(studying_list), disable_notification=1)
        bot.send_audio(message.chat.id, random.choice(studying_list), disable_notification=1)
        bot.send_sticker(message.chat.id, 'CAADAgADFAkAAlwCZQOykwORp3AchRYE')

    elif message.text.lower() == 'poetry':
        bot.send_audio(message.chat.id, 'CQADAgADLQcAAkn80Evi9KmmqvCqIhYE', disable_notification=1)
        bot.send_audio(message.chat.id, 'CQADAgAD2gQAAuKn2EvH5XFV329_sBYE', disable_notification=1)
        bot.send_audio(message.chat.id, 'CQADAgADLgcAAkn80EuRCVTz5CcrlRYE', disable_notification=1)
        bot.send_audio(message.chat.id, 'CQADAgADLwcAAkn80EvU12_SsfarvBYE', disable_notification=1)
        bot.send_sticker(message.chat.id, 'CAADAgADHQADijc4AAEw0RBgpCTPAAEWBA')


        #Выбор для жанра
    elif message.text.lower() == 'по жанрам':
        bot.send_message(message.chat.id, 'Какой ты хочешь жанр?', reply_markup=keyboard_genre)
    elif message.text.lower() == 'pop':
        bot.send_audio(message.chat.id, random.choice(pop_list), disable_notification=1)
        bot.send_audio(message.chat.id, random.choice(pop_list), disable_notification=1)
        bot.send_audio(message.chat.id, random.choice(pop_list), disable_notification=1)
        bot.send_audio(message.chat.id, random.choice(pop_list), disable_notification=1)
        bot.send_audio(message.chat.id, random.choice(pop_list), disable_notification=1)
        #bot.send_sticker(message.chat.id, '')

    elif message.text.lower() == 'альтернатива':
        bot.send_audio(message.chat.id, random.choice(alternative_list), disable_notification=1)
        bot.send_audio(message.chat.id, random.choice(alternative_list), disable_notification=1)
        bot.send_audio(message.chat.id, random.choice(alternative_list), disable_notification=1)
        bot.send_audio(message.chat.id, random.choice(alternative_list), disable_notification=1)
        #bot.send_sticker(message.chat.id, '')

    elif message.text.lower() == 'рок':
        bot.send_audio(message.chat.id, random.choice(rock_list), disable_notification=1)
        bot.send_audio(message.chat.id, random.choice(rock_list), disable_notification=1)
        bot.send_audio(message.chat.id, random.choice(rock_list), disable_notification=1)
        bot.send_audio(message.chat.id, random.choice(rock_list), disable_notification=1)
        bot.send_audio(message.chat.id, random.choice(rock_list), disable_notification=1)
        #bot.send_sticker(message.chat.id, '')

    elif message.text.lower() == 'r&b':
        bot.send_audio(message.chat.id, random.choice(), disable_notification=1)
        bot.send_audio(message.chat.id, random.choice(), disable_notification=1)
        bot.send_audio(message.chat.id, random.choice(), disable_notification=1)
        bot.send_audio(message.chat.id, random.choice(), disable_notification=1)
        bot.send_audio(message.chat.id, random.choice(), disable_notification=1)
        #bot.send_sticker(message.chat.id, '')

    elif message.text.lower() == 'электроника':
        bot.send_audio(message.chat.id, random.choice(), disable_notification=1)
        bot.send_audio(message.chat.id, random.choice(), disable_notification=1)
        #bot.send_sticker(message.chat.id, '')




    else:
        bot.send_sticker(message.chat.id, 'CAADAgADNAADkp8eEfIdTHZlMTXQFgQ')


bot.polling(none_stop = True, interval = 0)


