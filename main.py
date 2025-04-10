
import os
import time
import schedule
from telegram import Bot
from dotenv import load_dotenv

# Завантаження змінних середовища
load_dotenv()
TOKEN = os.getenv("TELEGRAM_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

bot = Bot(token=TOKEN)

def send_signal():
    try:
        bot.send_message(chat_id=CHAT_ID, text="📈 Новий сигнал з Telegram-бота!")
        print("✅ Повідомлення надіслано")
    except Exception as e:
        print(f"❌ Помилка: {e}")

send_signal()
schedule.every(5).minutes.do(send_signal)

while True:
    schedule.run_pending()
    time.sleep(1)
