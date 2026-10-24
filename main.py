import telebot, random
from datetime import datetime
import threading
from flask import Flask

TOKEN = "8832090946:AAGjLlbNE-ORqNrRUIuLafozn9vNl3wGrUU"
bot = telebot.TeleBot(TOKEN)

app = Flask('')
@app.route('/')
def home(): return "ARAFAT VAI VIP BOT IS LIVE"

def run_flask():
    app.run(host='0.0.0.0', port=8080)

@bot.message_handler(commands=['start','signal'])
def signal(message):
    sig = random.choice(['BIG 🟢', 'SMALL 🔴'])
    number = random.randint(0, 9)
    time = datetime.now().strftime("%I:%M:%S %p")
    text = f"🔥 𝐀𝐑𝐀𝐅𝐀𝐓 𝐕𝐀𝐈 𝐕𝐈𝐏 𝐒𝐈𝐍𝐆𝐍𝐀𝐋 🔥\n━━━━━━━━━━━━━━\n🎲 Number: {number}\n👉 SIGNAL: {sig}\n\n⏰ Time: {time}\n🎯 Accuracy: 99%\n📊 Mode: APEX\n━━━━━━━━━━━━━━\n👑 𝐀𝐑𝐀𝐅𝐀𝐓 | 𝐕𝐀𝐈\n𝐎𝐖𝐍𝐄𝐑 𝐈𝐃: @ARAFAT_VAI_D"
    bot.send_message(message.chat.id, text)

threading.Thread(target=run_flask).start()
bot.infinity_polling()
