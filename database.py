import aiomysql
from dotenv import load_dotenv
from os import getenv

load_dotenv()


async def create_pool():
    return await aiomysql.create_pool(
        host=getenv("DB_HOST"),
        user=getenv("DB_USER"),
        password=getenv("DB_PASSWORD"),
        db=getenv("DB_NAMEA"),
        autocommit=True,
        minsize=1,
        maxsize=5,
    )
