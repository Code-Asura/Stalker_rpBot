from aiogram.filters.callback_data import CallbackData

class Callback_Factory(CallbackData, prefix="call_f"):
    text: str
    user_id: int
    