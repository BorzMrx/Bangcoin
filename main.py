from aiogram import Bot, Dispatcher, types, executor
from aiogram.types import ParseMode
from config import  TELEGRAM_TOKEN
from aiogram.utils import executor

bot = Bot(token=TELEGRAM_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=("start"))
async def send_welcome(message: types.Message):
    welcome_message = (
        "👋 *Приветствуем вас в мире криптовалют с Bangcoin!* 🎉\n\n"
        "Я ваш надежный крипто-ассистент, готовый помочь вам покорить финансовые вершины. Воспользуйтесь моими возможностями:\n\n"
        "🚀 *Актуальные курсы* - Мгновенно узнавайте цены на ведущие криптовалюты.\n"
        "📊 *Глубокая аналитика* - Получайте точные прогнозы и подробные отчеты.\n"
        "📰 *Горячие новости* - Будьте в курсе последних событий и трендов.\n"
        "🔒 *Безопасность* - Защищенные и конфиденциальные консультации.\n\n"
        "Начните с команды /start, чтобы раскрыть полный потенциал Bangcoin. Не стесняйтесь задавать вопросы и исследовать мир криптовалют вместе со мной.\n\n"
        "Если вам нужна помощь, используйте команду /help, чтобы получить список доступных команд и их описание.\n\n"
        "🌟 *Bangcoin* - Ваш ключ к успеху в криптомире!"
    )
    await message.answer(welcome_message, parse_mode=ParseMode.MARKDOWN)

    @dp.message_handler(commands=("help"))
    async def send_help(message: types.Message):
        help_message = (
            "🆘 *Помощь по Bangcoin* 🆘\n\n"
            "Я здесь, чтобы помочь вам освоиться в мире криптовалют. Вот список команд, которые вы можете использовать:\n\n"
            "🔹 /start - Начать взаимодействие с ботом и получить приветственное сообщение.\n"
            "🔹 /help - Получить список доступных команд и их описание.\n"
            "🔹 /price [название_валюты] - Узнать текущий курс указанной криптовалюты.\n"
            "🔹 /forecast [название_валюты] - Получить прогноз и аналитику для выбранной криптовалюты.\n"
            "🔹 /news - Получить последние новости и обновления из мира криптовалют.\n"
            "🔹 /security - Советы и рекомендации по безопасности ваших крипто-активов.\n\n"
            "Если у вас возникли вопросы или предложения, не стесняйтесь обращаться!"
        )
        await message.answer(help_message, parse_mode=ParseMode.MARKDOWN)

@dp.message_handler(commands=["price"])
async def send_price(message: types.Message):
    price_message = (
        "💱 *Курс криптовалюты* 💱\n\n"
        "Используйте команду в формате `/price [название_валюты]`, чтобы узнать текущий курс указанной криптовалюты.\n\n"
        "Пример: `/price BTC`"
    )
    await message.answer(price_message, parse_mode=ParseMode.MARKDOWN)

@dp.message_handler(commands=["forecast"])
async def send_forecast(message: types.Message):
    forecast_message = (
        "🔮 *Прогноз курса криптовалюты* 🔮\n\n"
        "Используйте команду в формате `/forecast [название_валюты]`, чтобы получить прогноз и аналитику для выбранной криптовалюты.\n\n"
        "Пример: `/forecast ETH`"
    )
    await message.answer(forecast_message, parse_mode=ParseMode.MARKDOWN)

@dp.message_handler(commands=["news"])
async def send_news(message: types.Message):
    news_message = (
        "📰 *Новости криптовалют* 📰\n\n"
        "Используйте команду `/news`, чтобы получить последние новости и обновления из мира криптовалют."
    )
    await message.answer(news_message, parse_mode=ParseMode.MARKDOWN)

@dp.message_handler(commands=["security"])
async def send_security(message: types.Message):
    security_message = (
        "🔒 *Безопасность криптовалют* 🔒\n\n"
        "Используйте команду `/security`, чтобы получить советы и рекомендации по безопасности ваших крипто-активов."
    )
    await message.answer(security_message, parse_mode=ParseMode.MARKDOWN)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates= True)