import os, random, threading
from datetime import datetime
from flask import Flask
import telebot

# Render এর Environment থেকে টোকেন নেবে
BOT_TOKEN = os.environ.get("BOT_TOKEN") 
if not BOT_TOKEN:
    # যদি Environment এ না থাকে তাহলে তোমার টোকেনটা এখানে বসাবে
    BOT_TOKEN = "8803279285:AAHBCaJcQwBhkbF94WKsg6F-5wq7ng3etnk"

bot = telebot.TeleBot(BOT_TOKEN)
app = Flask(__name__)

@app.route('/')
def home():
    return "ARAFAT VIP BOT IS LIVE"

@bot.message_handler(commands=['start'])
def start(message):
    name = message.from_user.first_name
    text = f"🔥 𝐀𝐑𝐀𝐅𝐀𝐓 𝐕𝐀𝐈 𝐕𝐈𝐏 𝐒𝐈𝐍𝐆𝐍𝐀𝐋 🔥\n━━━━━━━━━━━━━━\n👋 Hello {name}!\n\n💎 Welcome To Arafat Vip Bot\n👑 Created By @ARAFAT_VAI_D\n\n📌 Commands:\n🎯 /signal - Get Signal\n🆘 /help - Help\n━━━━━━━━━━━━━━"
    bot.send_message(message.chat.id, text)

@bot.message_handler(commands=['signal'])
def signal(message):
    sig = random.choice(['BIG 🟢', 'SMALL 🔴'])
    number = random.randint(0, 9)
    time = datetime.now().strftime("%I:%M:%S %p")
    text = f"🔥 𝐀𝐑𝐀𝐅𝐀𝐓 𝐕𝐀𝐈 𝐕𝐈𝐏 𝐒𝐈𝐍𝐆𝐍𝐀𝐋 🔥\n━━━━━━━━━━━━━━\n🎲 Number: {number}\n👉 SIGNAL: {sig}\n\n⏰ Time: {time}\n🎯 Accuracy: 99%\n📊 Mode: APEX\n━━━━━━━━━━━━━━\n👑 𝐀𝐑𝐀𝐅𝐀𝐓 | 𝐕𝐀𝐈\n𝐎𝐖𝐍𝐄𝐑 𝐈𝐃: @ARAFAT_VAI_D"
    bot.send_message(message.chat.id, text)

@bot.message_handler(commands=['help'])
def help_cmd(message):
    bot.send_message(message.chat.id, "Just Send /signal - @ARAFAT_VAI_D")

def run_bot():
    print("Bot Started...")
    bot.infinity_polling()

if __name__ == "__main__":
    threading.Thread(target=run_bot, daemon=True).start()
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
    
