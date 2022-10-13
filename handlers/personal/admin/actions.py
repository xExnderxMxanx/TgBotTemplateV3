from aiogram import F, Router
from aiogram.types import Message

from fsm.filters import IsAdminUser

rt = Router()
rt.message.bind_filter(IsAdminUser)

@rt.message(F.chat.type == "private", is_admin=False)
async def message(message: Message):
    return await message.answer(message.text)