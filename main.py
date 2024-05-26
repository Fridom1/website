from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, Bot
from telegram.ext import Application, CommandHandler, CallbackQueryHandler

# Токен вашего бота
TOKEN = '7074822350:AAGCGnO6GoZsMVEGQ7J3BoIBr5t9Gmwj0bM'
WEB_APP_URL = 'https://your-web-app-url.com'  # Вставьте URL вашего веб-приложения
CHANNEL_URL = 'https://t.me/scamsociety'  # Вставьте правильный URL вашего канала


async def start(update: Update, context):
    chat_id = update.message.chat_id
    message = (
        "Привет! Добро пожаловать в Hamster Kombat 🎉\n"
        "Отныне ты — директор криптобиржи. Какой? Выбирай сам. "
        "Тапай по экрану, собирай монеты, качай пассивный доход, разрабатывай собственную стратегию дохода.\n"
        "Мы в свою очередь оценим это во время листинга токена, даты которого ты узнаешь совсем скоро.\n"
        "Про друзей не забывай — зови их в игру и получайте вместе ещё больше монет!"
    )

    keyboard = [
        [InlineKeyboardButton("Играть в 1 клик 🎮", web_app={'url': WEB_APP_URL})],
        [InlineKeyboardButton("Подписаться на канал", url=CHANNEL_URL)],
        [InlineKeyboardButton("Как заработать на игре", callback_data='earn')],
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(message, reply_markup=reply_markup)


async def button(update: Update, context):
    query = update.callback_query
    await query.answer()

    if query.data == 'earn':
        await query.edit_message_text(text="Вот как ты можешь заработать на игре...")


def main():
    # Создаем экземпляр приложения
    application = Application.builder().token(TOKEN).build()

    # Добавляем обработчики команд
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CallbackQueryHandler(button))

    # Запускаем бота
    application.run_polling()


if __name__ == '__main__':
    main()
