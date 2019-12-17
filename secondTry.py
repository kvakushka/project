import telebot


bot = telebot.TeleBot('947227617:AAEBlhomRlRuqeTymeM-zVo9Pn6JmxwgVf4')
keyboard = telebot.types.ReplyKeyboardMarkup()
keyboard.row('Привет', 'Пока', 'ты лох?')

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет, хочешь поговорить?', reply_markup=keyboard)

@bot.message_handler(commands=['song']) #для выяснения file_id у песен
def find_file_ids(message):
    for file in os.listdir('/Users/elinaaptineeva/Desktop/music/'):
        if file.split('.')[-1] == 'm4a':
            songg = open('/Users/elinaaptineeva/Desktop/music/'+file, 'rb')
            msg = bot.send_audio(message.chat.id, songg, None)
            bot.send_message(message.chat.id, msg.audio.file_id, reply_to_message_id=msg.message_id)
        time.sleep(1)

@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text.lower() == 'привет':
        bot.send_message(message.chat.id, 'Приветос')
    elif message.text.lower() == 'пока':
        bot.send_message(message.chat.id, 'Прощай......я буду скучать')
    elif message.text.lower() == 'ты лох?':
        bot.send_message(message.chat.id, 'сам ты лох, дебил')
    elif message.text.lower() == 'песенка': #просто проверочка
        bot.send_audio(message.chat.id, 'CQADAgADSQUAAkn8yEunFhTlnfi6khYE')
    else:
        bot.send_sticker(message.chat.id, 'CAADAgADNAADkp8eEfIdTHZlMTXQFgQ')



bot.polling(none_stop = True, interval = 0)


