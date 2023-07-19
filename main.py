import os
import telebot
from dotenv import load_dotenv
from commands import (
    handle_start,
    handle_selfie,
    handle_school_photo,
    handle_hobby,
    handle_wrong_command,
    send_voice_message,
    send_voice_menu,
)
from SpeechRecognition import handle_voice_message

load_dotenv()
bot = telebot.TeleBot(os.getenv("BOT_TOKEN"))

# Handlers
bot.message_handler(commands=["start"])(handle_start)
bot.message_handler(commands=["selfie"])(handle_selfie)
bot.message_handler(commands=["school_photo"])(handle_school_photo)
bot.message_handler(commands=["hobby"])(handle_hobby)
bot.message_handler(content_types=["voice"])(handle_voice_message)
bot.message_handler(func=lambda message: message.text == "Прислать войс")(
    send_voice_menu
)


@bot.callback_query_handler(func=lambda call: True)
def handle_callback(call):
    if call.data == "gpt":
        send_voice_message(call, "voice/GPT.opus")
    elif call.data == "sql_nosql":
        send_voice_message(call, "voice/sql.opus")
    elif call.data == "love":
        send_voice_message(call, "voice/love.opus")


bot.message_handler(func=lambda message: True)(handle_wrong_command)


bot.polling()
