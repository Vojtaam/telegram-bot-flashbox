from telebot import TeleBot
from telebot.types import BotCommand
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')
bot = TeleBot(TOKEN)

def register_commands(bot: TeleBot):
    commands = [
        BotCommand("start", "Start the bot"),
        BotCommand("hello", "Hello"),
        BotCommand("keyboard", "Open FlashBOX Mini App"),  # NOVÝ PŘÍKAZ
    ]
    
    bot.set_my_commands(commands)

if __name__ == "__main__":
    register_commands(bot)
    print("✅ Příkazy zaregistrovány!")
