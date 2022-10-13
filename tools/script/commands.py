from aiogram import Bot
from aiogram.types import BotCommand, BotCommandScopeAllPrivateChats

async def set_commands(bot: Bot):
    admin_comands = [
        BotCommand(command="/menu", description="Main bot menu"),
        BotCommand(command="/cancel", description="cancel the current operation")
    ]
    
    return await bot.set_my_commands(admin_comands, BotCommandScopeAllPrivateChats())