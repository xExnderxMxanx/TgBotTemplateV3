from aiogram.filters import BaseFilter
from aiogram.types import Message

from dispatcher import bot, conf

class IsAdminUser(BaseFilter):
    is_admin: bool
        
    async def __call__(self, message: Message) -> bool:
        member = await bot.get_chat_member(conf.bot.channel_id, message.from_user.id)
        return (member.status in ["creator", "admin"]) == self.is_admin