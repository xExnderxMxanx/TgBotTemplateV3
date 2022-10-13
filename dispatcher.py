import logging
import sys

from aiogram import Bot, Dispatcher
from aiogram.client.session.aiohttp import AiohttpSession
from aiogram.fsm.storage.redis import RedisStorage

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from loguru import logger

from tools.conf.config import load_config

conf = load_config("tools/conf/config.ini")

# Configure logger
logger.remove()

if conf.app.is_prod:
    logger.add(conf.app.path_log, level="INFO",
               format="<b><g>{time:%Y-%m-%d %r}</g>:<level>{level}</level>:<lw>{name}</lw>:<level>{message}</level></b>",
               colorize=True, rotation="4 week", compression="zip")
else:
    logger.add(sys.stderr, level="DEBUG", colorize=True,
               format="<b><g>{time:%Y-%m-%d %r}</g>:<level>{level}</level>:<lw>{name}</lw>:<level>{message}</level></b>")
    
class InterceptHandler(logging.Handler):
    def emit(self, record):
        # Get corresponding Loguru level if it exists.
        try:
            level = logger.level(record.levelname).name
        except ValueError:
            level = record.levelno

        # Find caller from where originated the logged message.
        frame, depth = sys._getframe(6), 6
        while frame and frame.f_code.co_filename == logging.__file__:
            frame = frame.f_back
            depth += 1

        logger.opt(depth=depth, exception=record.exc_info).log(level, record.getMessage())

logging.basicConfig(handlers=[InterceptHandler()], level=0, force=True)

# storage
storage = RedisStorage.from_url(conf.redis.url)

# init telegram BOt
bot = Bot(conf.bot.token, AiohttpSession(), "MarkdownV2")
dp = Dispatcher()

# init Database
engine = create_engine(conf.db.db_url)
model = declarative_base()
db_s = sessionmaker(bind=engine)()

