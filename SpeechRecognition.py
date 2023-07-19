import os
import assemblyai as aai
import telebot
from dotenv import load_dotenv

load_dotenv()
ASSEMBLYAI_API_KEY = os.getenv("ASSEMBLYAI_API_KEY")
bot = telebot.TeleBot(os.getenv("BOT_TOKEN"))


@bot.message_handler(content_types=["voice"])
def handle_voice_message(message):
    # Код обработки голосового сообщения
    file_info = bot.get_file(message.voice.file_id)
    file_url = f"https://api.telegram.org/file/bot{bot.token}/{file_info.file_path}"

    aai.settings.api_key = ASSEMBLYAI_API_KEY
    transcriber = aai.Transcriber()

    response = transcriber.transcribe(file_url)
    text = response.text

    bot.send_message(message.chat.id, f"Вы сказали: {text}")
