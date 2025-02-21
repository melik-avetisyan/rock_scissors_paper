from environs import Env
from dataclasses import dataclass


@dataclass
class TgBot:
    token: str


@dataclass
class DataBase:
    system_user: str
    password: str
    host: str
    dbname: str


@dataclass
class Config:
    tgbot: TgBot
    db: DataBase


def load_config(path: str | None = None) -> Config:

    env = Env()
    env.read_env(path)

    return Config(TgBot(token=env('BOT_TOKEN')),
                  DataBase(system_user=env('SYS_USER'),
                           password=env('PASSWORD'),
                           host=env('HOST'),
                           dbname=env('DB_NAME')))


