import telebot, random, string, os
from flask import Flask
from threading import Thread
import time

TOKEN = os.environ.get("BOT_TOKEN", "8832090946:AAGjLlbNE-ORqNrRU")
bot = telebot.TeleBot(TOKEN)
app = Flask('')
keys = {}

@app.route('/')
def home(): return "ARAFAT VAI VIP LIVE"

def run(): app.run(host='0.0.0.0', port=8080)
Thread(target=run).start()

@bot.message_handler(commands=['signal','start'])
def signal(m):
    n = random.randint(0,9)
    s = "BIG" if n>=5 else "SMALL"
    bot.reply_to(m, f"🔥 ARAFAT VAI VIP 🔥\n\nNumber: {n}\nSIGNAL: {s}\nAccuracy: 99%\n\nOwner: @ARAFAT_VAI_D")

@bot.message_handler(commands=['genkey'])
def genkey(m):
    txt = m.text.lower()
    days = 9999 if "life" in txt else 7
    pre = "VIPLIFE" if days>7 else "VIP7"
    code = ''.join(random.choices(string.ascii_uppercase+string.digits,k=7))
    key = f"{pre}-{code}"
    keys[key]=days
    bot.reply_to(m, f"✅ {days} দিনের Key:\n\n{key}")

while True:
    try:
        bot.infinity_polling(none_stop=True, timeout=60)
    except:
        time.sleep(5)
