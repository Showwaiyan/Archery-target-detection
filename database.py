import aiomysql
from dotenv import load_dotenv
from os import getenv

load_dotenv()

pool = None


async def init_pool():
    global pool
    pool = await aiomysql.create_pool(
        host=getenv("DB_HOST"),
        user=getenv("DB_USER"),
        password=getenv("DB_PASSWORD"),
        db=getenv("DB_NAME"),
        autocommit=True,
        minsize=1,
        maxsize=5,
    )


async def execute_query(sql: str, params=None):
    global pool
    if pool is None:
        raise RuntimeError("Database pool is not initialized")
    result = None

    async with pool.acquire() as conn:
        async with conn.cursor(aiomysql.DictCursor) as cursor:
            await cursor.execute(sql, params)
            return await cursor.fetchall()

    return result
