from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy import create_engine

# установка маршрута к БД
SQLALCHEMY_DATABASE_URL = "postgresql+asyncpg://postgres:postgres@localhost:5432/test_roboost_db"
SQLALCHEMY_SYNC_DATABASE_URL = "postgresql://postgres:postgres@localhost:5432/test_roboost_db"

engine = create_async_engine(SQLALCHEMY_DATABASE_URL)
sync_engine = create_engine(SQLALCHEMY_SYNC_DATABASE_URL)
SessionLocal = async_sessionmaker(
    autocommit=False, autoflush=False, bind=engine, expire_on_commit=False)
# создаёт класс сессии. принимает два параметра:
# autoflush: при значении True вызывается метод Session.flush(), записывающий все изменения в БД.
# bind: привязывает сессию БД к определённому движку, который применяется для установки подключения.


async def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        await db.close()
