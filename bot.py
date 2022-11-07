import asyncio

from loguru import logger

import handlers
from dispatcher import bot, dp
from utils.script.commands import set_commands

async def main() -> None:
    dp.include_router(handlers.rtAdmin)
    
    await set_commands(bot)
    try:
        await dp.start_polling(bot)
    except Exception as e:
        logger.error(e)
    finally:
        await dp.storage.close()
        await bot.session.close()
        logger.warning("Stoped")
        exit(0)

if __name__ == "__main__":
    asyncio.run(main())