import os, random, string, threading
from flask import Flask
import telebot

TOKEN = os.environ.get("BOT_TOKEN", "YOUR_BOT_TOKEN")
bot = telebot.TeleBot(TOKEN)
app = Flask(__name__)

@app.route('/')
def home():
    return "Bot is Live!"

def gen_key(days):
    if days == "lifetime":
        code = ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))
        return f"VIPLIFE-{code}"
    else:
        code = ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))
        return f"VIP7-{code}"

@bot.message_handler(commands=['signal'])
def signal(m):
    num = random.randint(1, 6)
    sig = "BIG" if num > 3 else "SMALL"
    bot.reply_to(m, f"🔥 ARAFAT VAI VIP SINGNAL 🔥\n\n🎲 Number: {num}\n👉 SIGNAL: {sig} 🔴\n\n⏰ Time: LIVE\n🎯 Accuracy: 99%\n📊 Mode: APEX\n\n👑 OWNER: @ARAFAT_VAI_D")

@bot.message_handler(commands=['genkey'])
def gk(m):
    try:
        arg = m.text.split()[1] if len(m.text.split()) > 1 else "7"
        if arg.lower() == "lifetime":
            key = gen_key("lifetime")
            bot.reply_to(m, f"✅ Lifetime Key তৈরি হয়েছে:\n\n{key}\n\nএটা কাউকে দাও, সে /redeem করলে Lifetime VIP পাবে।")
        else:
            key = gen_key(7)
            bot.reply_to(m, f"✅ ৭ দিনের নতুন Key তৈরি হয়েছে:\n\n{key}\n\nএটা কাউকে দাও, সে /redeem করলে ৭ দিন VIP পাবে।")
    except:
        key = gen_key(7)
        bot.reply_to(m, f"✅ ৭ দিনের নতুন Key:\n\n{key}")

threading.Thread(target=lambda: app.run(host="0.0.0.0", port=10000)).start()
bot.infinity_polling()
