import requests
from telebot import types

API_KEY = '340917bab50c8af5fd783da640a58931'


def try_search(searching_field):
    name_of_singer = searching_field
    url = f'http://ws.audioscrobbler.com/2.0/?method=artist.search&artist={name_of_singer}&api_key={API_KEY}&format=json'
    result_of_search = requests.get(url).json()
    return result_of_search


def preparing_message(source_message):
    name = source_message[0]['name']
    url = source_message[0]['url']
    bio = send_info(name)
    return (name, url, bio)


def send_info(singer):
    url = f'http://ws.audioscrobbler.com/2.0/?method=artist.getinfo&lang=ru&artist={singer}&api_key={API_KEY}&format=json'
    request_to = requests.get(url).json()
    bio = request_to['artist']['bio']['summary']
    return bio
