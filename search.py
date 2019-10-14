import requests
from telebot import types

API_KEY = '340917bab50c8af5fd783da640a58931'


def try_search():
    name_of_singer = 'Kendrick Lamar'
    url = f'http://ws.audioscrobbler.com/2.0/?method=artist.search&artist={name_of_singer}&api_key={API_KEY}&format=json'
    result_of_search = requests.get(url).json()
    return result_of_search

def preparing_message(source_message):
             
    name = artist_name['name']
    url = artist_url['url']
    return f'[{name}]({url})'