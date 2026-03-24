import telebot
import google.generativeai as genai
import os

# --- إعدادات الملك علي ---
# توكن البوت الخاص بك
CHITTY_TOKEN = '8573877624:AAEfusjbU-yH70sGU-5d-N9-eF8JTTb6c4o'

# مفتاح جيميناي (تأكد من وضعه هنا)
GEMINI_API_KEY = 'ضـع_مـفـتـاح_جـيـمـيـنـاي_هـنـا'

# إعداد ذكاء ماردوخ
genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel('gemini-1.5-flash')

bot = telebot.TeleBot(CHITTY_TOKEN)

@bot.message_handler(func=lambda message: True)
def marduk_response(message):
    try:
        # إرسال رسالة المستخدم لجيميناي
        response = model.generate_content(message.text)
        # رد ماردوخ على التلجرام
        bot.reply_to(message, response.text)
    except Exception as e:
        print(f"حدث خطأ: {e}")

if __name__ == "__main__":
    print("الملك ماردوخ استيقظ على السيرفر...")
    bot.polling(none_stop=True)
