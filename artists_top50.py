import requests
from telebot import types

API_KEY = '340917bab50c8af5fd783da640a58931'

# chart
def get_top_artist():
    url = f'http://ws.audioscrobbler.com/2.0/?method=chart.gettopartists&api_key={API_KEY}&format=json'
    top_50_artist = requests.get(url).json()
    return top_50_artist


def preparing_message(source_message):
    message = []
    for count, artist in enumerate(source_message):
        name = artist['name']
        artist_url = artist['url']
        
        message.append(f"{count + 1}. [{name}]({artist_url})")
    half_list_size = len(message) // 2
    return ["\r\n".join(message[:half_list_size]), "\r\n".join(message[half_list_size:])]


def make_inline_keyboard():
    inline_keyboard = types.InlineKeyboardMarkup(row_width=2)
    button_next = types.InlineKeyboardButton('→', callback_data='next')
    button_prev = types.InlineKeyboardButton('←', callback_data='prev')
    inline_keyboard.add(button_prev, button_next)
    return inline_keyboard