from configparser import ConfigParser
from dataclasses import dataclass

@dataclass
class App:
    version: str
    is_prod: bool
    path_log: str | None = None

@dataclass
class Bot:
    token: str
    chat_id: int
    channel_id: int
    
@dataclass
class Redis:
    url: str = "redis://localhost"

@dataclass
class DataBase:
    user: str
    db_name: str
    password: str
    db_url: str
    host: str = "localhost"
    port: str = "5432"
    
@dataclass
class Conf:
    app: App
    bot: Bot
    db: DataBase
    redis: Redis

def load_config(path: str) -> Conf:
    config = ConfigParser()
    config.read(path)
    
    app = {**config["APP"]} 
    app["is_prod"] = config["APP"].getboolean("is_prod")
    
    tg = {**config["TG"]} 
    tg["chat_id"] = config["TG"].getint("chat_id")
    tg["channel_id"] = config["TG"].getint("channel_id")

    return Conf(App(**app), Bot(**tg), DataBase(**config["DB"]),
                Redis(**config["REDIS"]))