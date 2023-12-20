from typing import Optional

from aiogram.filters.callback_data import CallbackData

class Callback_Factory(CallbackData, prefix="call_f"):
    text: Optional[str]
    user_id: Optional[str]
    