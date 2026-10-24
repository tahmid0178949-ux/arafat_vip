bot.reply_to(m, f"✅ ৭ দিনের নতুন Key তৈরি হয়েছে:\n\n{key}\n\nএটা কাউকে দাও, সে /redeem করলে ৭ দিন VIP পাবে।")
    except:
        key = gen_key(7)
        bot.reply_to(m, f"✅ ৭ দিনের নতুন Key:\n\n{key}")

threading.Thread(target=lambda: app.run(host="0.0.0.0", port=10000)).start()
bot.infinity_polling()

            
