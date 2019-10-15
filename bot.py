import telebot as tb
import proxy_changer
import lastfm
import artists_top50
import tracks_top50
import search
from telebot import types


proxy = proxy_changer.read_proxy()
bot = tb.TeleBot('940145749:AAENwzTWDnBkbCXwJZ8Fw7XdS0GCM5CgZoU', threaded=False)
tb.apihelper.proxy = proxy_changer.set_proxy(proxy)

user_data = {}


@bot.message_handler(commands=['start'])
def welcome(message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button_top_50_tracks = types.KeyboardButton('Топ 50 песен')
    button_top_50_artists = types.KeyboardButton('Топ 50 артистов')
    keyboard.add(button_top_50_tracks, button_top_50_artists)
    bot.send_message(message.chat.id, 'Выбери список Топ-50 песен или Топ 50 артистов', reply_markup=keyboard)


@bot.message_handler(content_types=['text'])
def send_text(message):

    if message.text.lower() == 'топ 50 песен':
        top_50_tracks = tracks_top50.get_top_tracks()
        msg = tracks_top50.preparing_message(top_50_tracks['tracks']['track'])
        user_data[message.chat.id] = msg
        inline_keyboard = tracks_top50.make_inline_keyboard()
        bot.send_message(message.chat.id, msg[0], reply_markup=inline_keyboard,
                         disable_web_page_preview=True, parse_mode='Markdown')

    elif message.text.lower() == 'топ 50 артистов':
        top_50_artists = artists_top50.get_top_artist()
        msg = artists_top50.preparing_message(top_50_artists['artists']['artist'])
        user_data[message.chat.id] = msg
        inline_keyboard = artists_top50.make_inline_keyboard()
        bot.send_message(message.chat.id, msg[0], reply_markup=inline_keyboard,
                         disable_web_page_preview=True, parse_mode='Markdown')



    else:
        try_search = search.try_search(message.text)
        msg = search.preparing_message(try_search['results']['artistmatches']['artist'])
        bot.send_message(message.chat.id, msg, disable_web_page_preview=True, parse_mode='Markdown')
        

@bot.callback_query_handler(func=lambda query: True)
def test(query):
    print(query)
    chat_id = query.message.chat.id
    if query.data == 'next':
        bot.edit_message_text(chat_id, user_data[chat_id][1], query.message.message_id)
    elif query.data == 'prev':
        bot.edit_message_text(chat_id, user_data[chat_id][0], query.message.message_id)


try:
    # Запускаем бота
    bot.polling()

# Если прокси отваливается
except OSError:
    bot.stop_polling()

    proxy = proxy_changer.get_proxy()
    proxy_changer.write_proxy(proxy)

    bot.polling()
