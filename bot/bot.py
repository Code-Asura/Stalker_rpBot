from aiogram import Bot, Dispatcher
from aiohttp import web
from aiogram.webhook.aiohttp_server import SimpleRequestHandler, setup_application

from data.config import config
from handlers import user_cmd

async def on_startup(bot: Bot):
    await bot.set_webhook(f"{config.webhook_domain}{config.webhook_path}")


def main():
    bot = Bot(config.token.get_secret_value())
    dp = Dispatcher()
    dp.include_router(user_cmd.router)
    dp.startup.register(on_startup)
    app = web.Application()
    webhook_requests_handler = SimpleRequestHandler(
        dispatcher=dp,
        bot=bot
    )
    webhook_requests_handler.register(app, path=config.webhook_path)
    setup_application(app, dp, bot=bot)
    web.run_app(app, host=config.web_host, port=config.web_port)


if __name__ == "__main__":
    main()
