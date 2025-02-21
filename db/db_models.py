from sqlalchemy import Integer
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy.ext.asyncio import AsyncAttrs, async_sessionmaker
from sqlalchemy.ext.asyncio import create_async_engine

from config.config import load_config


config = load_config()


DATABASE_URL = f'postgresql+asyncpg://{config.db.system_user}' \
               f':{config.db.password}@{config.db.host}/{config.db.dbname}'

engine = create_async_engine(DATABASE_URL)
Session = async_sessionmaker(engine, expire_on_commit=False)


class Base(AsyncAttrs, DeclarativeBase):
    __abstract__ = True


class Player(Base):

    __tablename__ = "player"

    player_id = mapped_column(Integer, primary_key=True)
    tg_id: Mapped[int]
    nickname: Mapped[str]
    scores: Mapped[int] = mapped_column(default=0)
    games: Mapped[int] = mapped_column(default=0)
