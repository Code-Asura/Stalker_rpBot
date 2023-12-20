from aiogram import Dispatcher, Router

from .users import user_cmd
from .moderation import alert, mute, ban, report
from .role_play import registation

def includer(dp: Dispatcher):
    dp.include_routers(
        user_cmd.router,
        ban.ban_unban_router
    )


# def register(router: Router):
#     router.message.register()
