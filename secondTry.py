import telebot
import os
import time
import random
import openpyxl


bot = telebot.TeleBot('947227617:AAEBlhomRlRuqeTymeM-zVo9Pn6JmxwgVf4')

workbook = openpyxl.load_workbook(filename="/Users/elinaaptineeva/Desktop/Music.xlsx")

#Ссылки на листы из Excel
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
electro_sheet = workbook["Electro_id"]
sleep_sheet = workbook["ForSleep_id"]
acoustics_sheet = workbook["Acoustics_id"]


#Листы с file_id, импортированные из Excel
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
electro_list = [electro_sheet.cell(row=i,column=1).value for i in range(1,5)]
sleep_list = [sleep_sheet.cell(row=i,column=1).value for i in range(1,15)]
acoustics_list = [acoustics_sheet.cell(row=i,column=1).value for i in range(1,21)]
season_list = ny_list + love_list + gym_list + sad_list + party_list + nostalgia_list + studying_list + acoustics_list

#Клавиатуры
keyboard_mood = telebot.types.ReplyKeyboardMarkup()
keyboard_mood.row('New Year', 'In love', 'Gym')
keyboard_mood.row('Party', 'Nostalgia', 'Studying')
keyboard_mood.row('Poetry', 'Sad', 'Назад')

keyboard_menu = telebot.types.ReplyKeyboardMarkup()
keyboard_menu.row('По настроению', 'По жанрам')
keyboard_menu.row('По времени года', 'Топ песен')
keyboard_menu.row('Для сна', 'Акустика')

keyboard_genre = telebot.types.ReplyKeyboardMarkup()
keyboard_genre.row('Pop', 'Alternative')
keyboard_genre.row('Rock', 'Electronic', 'Назад')

keyboard_season = telebot.types.ReplyKeyboardMarkup()
keyboard_season.row('Зима', 'Весна')
keyboard_season.row('Лето', 'Осень')
keyboard_season.row('Назад')


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет, как ты хочешь осуществить выбор музыки?', reply_markup=keyboard_menu)


@bot.message_handler(commands=['song']) #команда для добавления новой песни(измените путь на свой, чтобы добавить)
def find_file_ids(message):
    for file in os.listdir('/Users/elinaaptineeva/Desktop/top/'):
        if file.split('.')[-1] == 'm4a' or 'mp3':
            songg = open('/Users/elinaaptineeva/Desktop/top/'+file, 'rb')
            msg = bot.send_audio(message.chat.id, songg, None)
            bot.send_message(message.chat.id, msg.audio.file_id, reply_to_message_id=msg.message_id)
        time.sleep(30)


print(acoustics_list)
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
        bot.send_audio(message.chat.id, random.choice(ny_list), disable_notification=1) #поэтому приходится пять раз отправлять разные сообщения с рандомными аудио
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
        bot.send_sticker(message.chat.id, 'CAADAgAD4AADtvArFMBb0Az0846ZFgQ')

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
        bot.send_sticker(message.chat.id, 'CAADAgADWQADaUCAC9ndtD9ic3QGFgQ')

    elif message.text.lower() == 'alternative':
        bot.send_audio(message.chat.id, random.choice(alternative_list), disable_notification=1)
        bot.send_audio(message.chat.id, random.choice(alternative_list), disable_notification=1)
        bot.send_audio(message.chat.id, random.choice(alternative_list), disable_notification=1)
        bot.send_audio(message.chat.id, random.choice(alternative_list), disable_notification=1)
        bot.send_sticker(message.chat.id, 'CAADAgADSQcAAlwCZQOcqEkLQYXIJxYE')

    elif message.text.lower() == 'electronic':
        bot.send_audio(message.chat.id, 'CQADAgADYwUAAuGH4EtRl5hpVDSCZRYE', disable_notification=1)
        bot.send_audio(message.chat.id, 'CQADAgADXwUAAuGH4EvWHODI_0btSRYE', disable_notification=1)
        bot.send_audio(message.chat.id, 'CQADAgAD1gQAAiqh2EsK2Y9yL33fJRYE', disable_notification=1)
        bot.send_audio(message.chat.id, 'CQADAgADrQUAArqK2EtjWFZkn6iYWhYE', disable_notification=1)
        bot.send_audio(message.chat.id, 'CQADAgADYgUAAuGH4Ev7kQnQeH-SrhYE', disable_notification=1)
        bot.send_sticker(message.chat.id, 'CAADAgADDwADdVCBE8INUWYwyF1_FgQ')

    elif message.text.lower() == 'rock':
        bot.send_audio(message.chat.id, random.choice(rock_list), disable_notification=1)
        bot.send_audio(message.chat.id, random.choice(rock_list), disable_notification=1)
        bot.send_audio(message.chat.id, random.choice(rock_list), disable_notification=1)
        bot.send_audio(message.chat.id, random.choice(rock_list), disable_notification=1)
        bot.send_audio(message.chat.id, random.choice(rock_list), disable_notification=1)
        bot.send_sticker(message.chat.id, 'CAADAgADAQQAAlrjihfEzKzoI5AMFBYE')

    #Топ песен
    elif message.text.lower() == 'топ песен':
        bot.send_message(message.chat.id, 'Топ любимых песен @theyoungestkvakushka. Плейлист не имеет отношения'
                                          'к топ-чартам. Песни могут не понравиться, как и любые другие :)')
        bot.send_audio(message.chat.id, 'CQADAgAD_gQAAiqh2Euk0Zlz9RVrrhYE', disable_notification=1)
        bot.send_audio(message.chat.id, 'CQADAgADugUAAuGH4EvSDUJyiZCBnBYE', disable_notification=1)
        bot.send_audio(message.chat.id, 'CQADAgADvAUAAuGH4EsnBK5djJMcyhYE', disable_notification=1)
        bot.send_audio(message.chat.id, 'CQADAgADvgUAAuGH4EuhG2N8by98LxYE', disable_notification=1)
        bot.send_audio(message.chat.id, 'CQADAgADAgUAAiqh2Et8CxPi0F3hSRYE', disable_notification=1)
        bot.send_sticker(message.chat.id, 'CAADAgADEQADKiVgENAXoI3E2CNbFgQ')

    #Акустика
    elif message.text.lower() == 'акустика':
        bot.send_audio(message.chat.id, random.choice(acoustics_list), disable_notification=1)
        bot.send_audio(message.chat.id, random.choice(acoustics_list), disable_notification=1)
        bot.send_audio(message.chat.id, random.choice(acoustics_list), disable_notification=1)
        bot.send_audio(message.chat.id, random.choice(acoustics_list), disable_notification=1)
        bot.send_sticker(message.chat.id, 'CAADAgADkQEAAhZ8aAOvQi9_OnNHJxYE')

    #Для сна
    elif message.text.lower() == 'для сна':
        bot.send_audio(message.chat.id, random.choice(sleep_list), disable_notification=1)
        bot.send_audio(message.chat.id, random.choice(sleep_list), disable_notification=1)
        bot.send_audio(message.chat.id, random.choice(sleep_list), disable_notification=1)
        bot.send_sticker(message.chat.id, 'CAADAgADCAEAAhgdBg_nlhA3Md1uwBYE')

    #По времени года
    elif message.text.lower() == 'по времени года':
        bot.send_message(message.chat.id, 'Выбери время года', reply_markup=keyboard_season)
        bot.send_sticker(message.chat.id, 'CAADBAADaAADL9_4CfYP_B84loBaFgQ')
    elif message.text.lower() == 'зима':
        bot.send_audio(message.chat.id, random.choice(season_list), disable_notification=1)
    elif message.text.lower() == 'весна':
        bot.send_audio(message.chat.id, random.choice(season_list), disable_notification=1)
    elif message.text.lower() == 'лето':
        bot.send_audio(message.chat.id, random.choice(season_list), disable_notification=1)
    elif message.text.lower() == 'осень':
        bot.send_audio(message.chat.id, random.choice(season_list), disable_notification=1)
    else:
        bot.send_sticker(message.chat.id, 'CAADAgADNAADkp8eEfIdTHZlMTXQFgQ')


bot.polling(none_stop = True, interval = 0)


