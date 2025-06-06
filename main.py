import os
import telebot
from telebot.types import ReplyKeyboardMarkup, KeyboardButton, WebAppInfo
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Replace 'TELEGRAM_BOT_TOKEN' with the token you received from BotFather
TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')
bot = telebot.TeleBot(TOKEN)

# URL tvé Mini Appky - ZMĚŇ NA SVOU URL!
WEBAPP_URL = "https://vojtaam.github.io/flashbox-mini-app/"

@bot.message_handler(commands=['start', 'hello'])
def send_welcome(message):
    bot.reply_to(message, "Hello! I'm FlashBOX bot. Use /keyboard to open Mini App.")

@bot.message_handler(commands=['keyboard'])
def send_keyboard(message):
    """Pošle keyboard button pro spuštění FlashBOX Mini Appky"""
    # Vytvoření keyboard buttonu s WebApp
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
    web_app_button = KeyboardButton("Open", web_app=WebAppInfo(url=WEBAPP_URL))
    keyboard.add(web_app_button)
    
    bot.send_message(
        message.chat.id,
        "Klikněte na tlačítko pro otevření FlashBOX Mini Appky:",
        reply_markup=keyboard
    )

@bot.message_handler(content_types=['web_app_data'])
def handle_web_app_data(message):
    """Handler pro data z Mini Appky"""
    # Zde zpracuješ data z Mini Appky
    data = message.web_app_data.data
    bot.reply_to(message, f"Přijatá data z FlashBOX: {data}")
    
    # Můžeš data přeposlat do skupiny nebo zpracovat podle potřeby
    # Například: bot.send_message(GROUP_CHAT_ID, f"FlashBOX: {data}")

@bot.message_handler(func=lambda msg: True)
def echo_all(message):
    # Původní echo funkce zůstává
    bot.reply_to(message, message.text)

if __name__ == "__main__":
    print("🤖 FlashBOX Bot spuštěn...")
    bot.polling()
