import os
import telebot
from dotenv import load_dotenv
from telebot import types

load_dotenv()
bot = telebot.TeleBot(os.getenv("BOT_TOKEN"))


def handle_start(message):
    bot.send_message(message.chat.id, "Привет! Я Человек), давай познакомимся.")
    bot.send_message(
        message.chat.id,
        "Чтобы узнать больше обо мне, воспользуйтесь кнопками ниже. Можешь узнать о мое "
        "хобби введи команду /hobby",
    )


def handle_selfie(message):
    # команда /selfie
    with open("image/IMG_4796.JPG", "rb") as photo:
        bot.send_photo(message.chat.id, photo)


def handle_school_photo(message):
    # команда /school_photo
    with open("image/IMG_1245.PNG", "rb") as photo:
        bot.send_photo(message.chat.id, photo)


def handle_hobby(message):
    # команда /hobby
    bot.send_message(
        message.chat.id,
        "Мое главное увлечение - это музыка. Играю на гитаре и на пианино и пою. Стремлюсь к тому чтобы "
        "стать человеком оркестром",
    )


def handle_wrong_command(message):
    bot.send_message(message.chat.id, "Ошибка! Неизвестная команда.")


def send_voice_menu(message):
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    gpt_button = types.InlineKeyboardButton("GPT", callback_data="gpt")
    sql_button = types.InlineKeyboardButton("SQL и NoSQL", callback_data="sql_nosql")
    love_button = types.InlineKeyboardButton(
        "История первой любви", callback_data="love"
    )
    keyboard.add(gpt_button, sql_button, love_button)

    bot.send_message(
        message.chat.id, "Выберите голосовое сообщение:", reply_markup=keyboard
    )


def send_voice_message(call, filename):
    with open(filename, "rb") as voice_file:
        bot.send_voice(call.message.chat.id, voice_file, reply_markup=None)
