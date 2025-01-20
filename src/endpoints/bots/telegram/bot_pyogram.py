from pyrogram import Client, filters
import os

# Замените на свои значения
API_ID = int(os.environ.get("TELEGRAM_API_ID",''))
API_HASH = os.environ.get("TELEGRAM_API_HASH",'')
BOT_TOKEN = os.environ.get("TELEGRAM_TOKEN",'')


# Создаем экземпляр клиента Pyrogram
app = Client(
    "my_simple_bot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

# Обработчик команды /start
@app.on_message(filters.command("start"))
def start_command(client, message):
    message.reply_text("Привет! Я простой бот на Pyrogram.")

# Обработчик всех текстовых сообщений (кроме команд)
@app.on_message(filters.text & ~filters.command)
def echo_message(client, message):
    message.reply_text(message.text)

# Запуск бота
if __name__ == "__main__":
    print("Бот запущен...")
    app.run()