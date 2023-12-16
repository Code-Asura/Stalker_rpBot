from aiogram import Bot, Dispatcher
from aiohttp import web
from aiogram.webhook.aiohttp_server import SimpleRequestHandler, setup_application

from data.config import config
from handlers import user_cmd

#TODO Установка вебхука
async def on_startup(bot: Bot):
    await bot.set_webhook(f"{config.webhook_domain}{config.webhook_path}")

#TODO Запуск веб сервера с ботом
def main():
    bot = Bot(config.token.get_secret_value()) #?Бот
   
    dp = Dispatcher() #? Диспетчер 
    dp.include_router(user_cmd.router) #? Функция подключения роутеров
    dp.startup.register(on_startup) #? Регистрация стартовой функции
    
    app = web.Application() #? Веб приложение
    webhook_requests_handler = SimpleRequestHandler( 
        dispatcher=dp,
        bot=bot
    ) #? Распределитель обновлений ⬆ 
    
    webhook_requests_handler.register(app, path=config.webhook_path) #? Регистрация хендлера вебхуков
    setup_application(app, dp, bot=bot)
    web.run_app(app, host=config.web_host, port=config.web_port) #? Запуск веб приложения


#! Проверка запуска текущего файла
if __name__ == "__main__": 
    main()
