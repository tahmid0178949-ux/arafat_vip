import os, random, string, threading
from flask import Flask
import telebot

BOT_TOKEN = os.environ.get("BOT_TOKEN")
bot = telebot.TeleBot(BOT_TOKEN)
app = Flask(__name__)

@app.route('/')
def home():
    return "Bot is Live"

def make_key(prefix):
    code = ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))
    return f"{prefix}-{code}"

@bot.message_handler(commands=['signal'])
def signal_cmd(m):
    num = random.randint(0, 9)
    sig = "BIG" if num >= 5 else "SMALL"
    bot.reply_to(m, f"🔥 ARAFAT VIP SIGNAL 🔥\nNumber: {num}\nSignal: {sig}")

@bot.message_handler(commands=['genkey'])
def genkey_cmd(m):
    parts = m.text.split()
    arg = parts[1].lower() if len(parts) > 1 else "7"
    if arg == "lifetime":
        key = make_key("VIPLIFE")
        bot.reply_to(m, f"✅ Lifetime Key:\n\n{key}")
    else:
        key = make_key("VIP7")
        bot.reply_to(m, f"✅ 7 Day Key:\n\n{key}")

def run_bot():
    bot.infinity_polling()

if __name__ == "__main__":
    threading.Thread(target=run_bot, daemon=True).start()
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
