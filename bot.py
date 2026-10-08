import telebot

# تنظیمات ربات
TOKEN = '8887687811:AAHTEHRH_x6DgggKFsCCw4jBdnF3m4d62Mk'
CHANNEL_USERNAME = '@amirnafarieh_co' 
PRIVATE_CHANNEL_ID = -1000000000000 # بعدا باید این عدد را با آیدی کانال انبار خودت عوض کنی

bot = telebot.TeleBot(TOKEN)

def is_subscribed(user_id):
    try:
        status = bot.get_chat_member(CHANNEL_USERNAME, user_id).status
        return status in ['member', 'administrator', 'creator']
    except:
        return False

@bot.message_handler(commands=['start'])
def send_file(message):
    user_id = message.chat.id
    command_text = message.text.split()

    if not is_subscribed(user_id):
        bot.send_message(user_id, f"⭕️ برای دانلود فایل‌های پروژه، ابتدا در کانال {CHANNEL_USERNAME} عضو شو و بعد دوباره روی لینک کلیک کن.")
        return

    if len(command_text) > 1:
        file_message_id = command_text[1]
        try:
            bot.copy_message(user_id, PRIVATE_CHANNEL_ID, int(file_message_id))
        except:
            bot.send_message(user_id, "❌ فایل پیدا نشد یا از سرور پاک شده است.")
    else:
        bot.send_message(user_id, "✅ به ربات دریافت پروژه‌های آماده خوش آمدی.")

bot.infinity_polling()
