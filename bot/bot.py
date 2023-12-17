import asyncio

from aiogram import Bot, Dispatcher
from aiohttp import web
from aiogram.webhook.aiohttp_server import SimpleRequestHandler, setup_application

from data.config import config
from handlers import user_cmd

#TODO Стартовая функция
async def on_startup(bot: Bot):
    if not config.webhook_domain:
        await bot.set_webhook(f"{config.custom_webhook_domain}{config.custom_webhook_path}",
                                drop_pending_updates=True)
    
    else:
        await bot.set_webhook(f"{config.webhook_domain}{config.webhook_path}",
                                drop_pending_updates=True)
        

async def start_pooling_bot(bot: Bot, dp: Dispatcher):
    await bot.delete_webhook(drop_pending_updates=True)

    await dp.start_polling(bot)


def main():
    bot = Bot(config.token.get_secret_value()) #?Бот

    dp = Dispatcher() #? Диспетчер 
    dp.include_router(user_cmd.router) #? Функция подключения роутеров

    try:
        #? Проверка на тип запуска бота
        if not config.webhook_domain and not config.custom_webhook_domain:
            asyncio.run(start_pooling_bot(bot, dp))

        else:
            dp.startup.register(on_startup) #? Регистрация стартовой функции

            app = web.Application() #? Веб приложение
            webhook_requests_handler = SimpleRequestHandler( 
                dispatcher=dp,
                bot=bot
            ) #? Распределитель обновлений ⬆ 
            
            #? Проверка пути для регистрации обработчика
            if not config.custom_webhook_path:
                webhook_requests_handler.register(app, path=config.webhook_path) #? Регистрация хендлера вебхуков
            
            else: 
                webhook_requests_handler.register(app, path=config.custom_webhook_path) #? Регистрация хендлера вебхуков
                
            setup_application(app, dp, bot=bot)
            web.run_app(app, host=config.web_host, port=config.web_port)

    finally:
        asyncio.run(bot.session.close())


#! Проверка запуска текущего файла
if __name__ == "__main__": 
    main()
