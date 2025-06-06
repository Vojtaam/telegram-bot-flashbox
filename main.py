import os
import telebot
from telebot.types import ReplyKeyboardMarkup, KeyboardButton, WebAppInfo, InlineKeyboardMarkup, InlineKeyboardButton
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')
bot = telebot.TeleBot(TOKEN)
WEBAPP_URL = "https://vojtaam.github.io/flashbox-mini-app/"

@bot.message_handler(commands=['start', 'hello'])
def send_welcome(message):
    bot.reply_to(message, "🔵 Vítejte ve FlashBOX! Pro otevření aplikace použijte /keyboard")

@bot.message_handler(commands=['keyboard'])
def send_keyboard(message):
    """Inteligentní rozpoznání typu chatu"""
    if message.chat.type in ["private", "group", "supergroup"]:
        if message.chat.type == "private":
            # Privátní chat - Keyboard Button
            keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
            web_app_button = KeyboardButton("🔵 Otevřít FlashBOX", web_app=WebAppInfo(url=WEBAPP_URL))
            keyboard.add(web_app_button)
            
            bot.send_message(
                message.chat.id,
                "Klikněte na tlačítko pro otevření aplikace:",
                reply_markup=keyboard
            )
        else:
            # Skupinový chat - Inline Button s odkazem
            keyboard = InlineKeyboardMarkup()
            web_app_button = InlineKeyboardButton(
                "🔵 Otevřít FlashBOX", 
                url=f"https://t.me/{bot.get_me().username}?startapp=flashbox"
            )
            keyboard.add(web_app_button)
            
            bot.send_message(
                message.chat.id,
                "Pro otevření FlashBOX aplikace klikněte na tlačítko níže:",
                reply_markup=keyboard
            )

@bot.message_handler(content_types=['web_app_data'])
def handle_web_app_data(message):
    """Zpracování dat pouze z privátních chatů"""
    if message.chat.type == "private":
        data = message.web_app_data.data
        bot.reply_to(message, f"✅ Data přijata: {data}")
        # Zde implementujte odeslání do skupiny/n8n
    else:
        bot.reply_to_message(message, "❌ Data lze přijímat pouze v privátním chatu")

if __name__ == "__main__":
    print("🤖 FlashBOX Bot úspěšně spuštěn!")
    bot.polling()
