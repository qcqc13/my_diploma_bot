import telebot as tb
import proxy_changer
import lastfm
from telebot import types


proxy = proxy_changer.read_proxy()
bot = tb.TeleBot('940145749:AAENwzTWDnBkbCXwJZ8Fw7XdS0GCM5CgZoU', threaded=False)
tb.apihelper.proxy = proxy_changer.set_proxy(proxy)



@bot.message_handler(commands=['start'])
def welcome(message):
    markup = types.ReplyKeyboardMarkup(True, True)
    itembtn1 = types.KeyboardButton('Топ 50 песен')
    itembtn2 = types.KeyboardButton('Топ 50 артистов')
    markup.add(itembtn1, itembtn2)
    bot.send_message(message.chat.id,'Выбери список Топ-50 песен или Топ 50 артистов', reply_markup=markup)

@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text.lower() == 'топ 50 песен':
        top_50_artists = lastfm.get_top_artist()
        msg = lastfm.preparing_message(top_50_artists['artists']['artist'])
        bot.send_message(message.chat.id, msg, disable_web_page_preview=True, parse_mode='Markdown')

    elif message.text.lower() == 'топ 50 артистов':
        bot.send_message(message.chat.id, 'Прощай, создатель')

    else:
        bot.reply_to(message, 'Не понимаю, но салам')


try:
    # Запускаем бота
    bot.polling()

# Если прокси отваливается
except OSError:
    bot.stop_polling()

    proxy = proxy_changer.get_proxy()
    proxy_changer.write_proxy(proxy)

    bot.polling()
