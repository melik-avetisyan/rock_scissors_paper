from sqlalchemy import select
from db.db_models import engine, Session, Base, Player


async def db_conn():
    async with engine.begin() as conn:
        #await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)


def connection(func):
    async def wrapper(*args, **kwargs):
        async with Session() as session:
            return await func(*args, session=session, **kwargs)
    return wrapper


@connection
async def add_player(message, session=None):
    query = select(Player).where(Player.tg_id == message.from_user.id)
    res = await session.execute(query)
    if not res.one_or_none():
        session.add(Player(tg_id=message.from_user.id,
                           nickname=message.from_user.username))
        await session.commit()


@connection
async def set_resul(message, session=None, score=0):
    query = select(Player).where(Player.tg_id == message.from_user.id)
    res = await session.execute(query)
    player = res.scalar()
    player.games += 1
    player.scores += score
    await session.commit()


@connection
async def get_stat(id, session=None):
    query = select(Player).where(Player.tg_id == id)
    res = await session.execute(query)
    player = res.scalar()
    return player
