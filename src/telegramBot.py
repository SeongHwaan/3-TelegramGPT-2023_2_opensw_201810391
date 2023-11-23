from dotenv import load_dotenv
import os 
import sys
import telegram
import asyncio
import telegram
from telegram.ext import Application, MessageHandler, filters
from gpt import chatgpt


load_dotenv()

token = os.environ.get('telegramToken')
chatId = os.environ.get('chatId')
bot = telegram.Bot(token = token)
public_chat_name = '@Open2023test'

    
async def echo(update, context):
    user_text = update.channel_post.text
    await bot.send_message(chat_id=public_chat_name, text=chatgpt(user_text))

def main():
    application = Application.builder().token(token).build()
    application.add_handler(MessageHandler(filters.ALL, echo))
    application.run_polling(1.0)

if __name__ == "__main__":
    main()
