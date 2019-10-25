import requests
from telebot import types

API_KEY = '340917bab50c8af5fd783da640a58931'

def get_top_tracks():
    url = f'http://ws.audioscrobbler.com/2.0/?method=chart.gettoptracks&api_key={API_KEY}&format=json'
    top_50_tracks = requests.get(url).json()
    return top_50_tracks


def preparing_message(source_message):
    message = []
    for count, track in enumerate(source_message):
        singer = track['artist']['name']
        name = track['name']
        track_url = track['url']
        
        message.append(f'{count + 1}. {singer} – [{name}]({track_url})')
    half_list_size = len(message) // 2
    return ['\r\n'.join(message[:half_list_size]), '\r\n'.join(message[half_list_size:])]


def make_inline_keyboard():
    inline_keyboard = types.InlineKeyboardMarkup(row_width=2)
    button_next = types.InlineKeyboardButton('→', callback_data='next')
    button_prev = types.InlineKeyboardButton('←', callback_data='prev')
    inline_keyboard.add(button_prev, button_next)
    return inline_keyboard