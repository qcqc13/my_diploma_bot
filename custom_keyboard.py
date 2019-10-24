from telebot import types


def make_navigator(without_button=None):
    inline_keyboard = types.InlineKeyboardMarkup(row_width=2)
    if without_button == 'right':
        button_prev = types.InlineKeyboardButton('←', callback_data='prev')
        inline_keyboard.add(button_prev)
        return inline_keyboard
    elif without_button == 'left':
        button_next = types.InlineKeyboardButton('→', callback_data='next')
        inline_keyboard.add(button_next)
        return inline_keyboard
    else:
        button_next = types.InlineKeyboardButton('→', callback_data='next')
        button_prev = types.InlineKeyboardButton('←', callback_data='prev')
        inline_keyboard.add(button_prev, button_next)
        return inline_keyboard


def make_top_50():
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button_top_50_tracks = types.KeyboardButton('Топ 50 песен')
    button_top_50_artists = types.KeyboardButton('Топ 50 артистов')
    keyboard.add(button_top_50_tracks, button_top_50_artists)
    return keyboard


def make_artist_page(artist_url):
    inline_keyboard = types.InlineKeyboardMarkup()
    page_link_button = types.InlineKeyboardButton('Открыть на last.fm', url=artist_url)
    inline_keyboard.add(page_link_button)
    return inline_keyboard