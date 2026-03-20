from telethon import TelegramClient, events
import os
from flask import Flask
import threading

# إعدادات بسيطة لتشغيل السيرفر
app = Flask(__name__)
@app.route('/')
def hello():
    return "Marduk is Running!"

def run_flask():
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))

# بيانات التليجرام (سيتم ربطها لاحقاً)
API_ID = os.environ.get('API_ID')
API_HASH = os.environ.get('API_HASH')
BOT_TOKEN = os.environ.get('BOT_TOKEN')

client = TelegramClient('marduk_session', API_ID, API_HASH).start(bot_token=BOT_TOKEN)

@client.on(events.NewMessage(pattern='/start'))
async def start(event):
    await event.reply('مرحباً بك! نظام ماردوخ يعمل الآن على السحاب بنجاح. 👑')

if __name__ == '__main__':
    threading.Thread(target=run_flask).start()
    print("Marduk System Started...")
    client.run_until_disconnected()
