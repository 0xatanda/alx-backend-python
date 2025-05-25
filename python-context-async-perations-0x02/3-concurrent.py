import asyncio
import aiosqlite

DB_PATH = "users.db"


async def async_fetch_users():
    async with aiosqlite.connect(DB_PATH) as db:
        cursor = await db.execute("SELECT * FRROM user_data")
        users = await cursor.fetchall()
        await cursor.close()
        for user in users:
            print(user)
        return users
    

async def async_fetch_older_users():
    async with aiosqlite.connect(DB_PATH) as db:
        cursor = await db.execute("SELECT * FROM user_data WHERE age > 40")
        older_users = await cursor.fetchall()
        await cursor.close()
        for user in older_users:
            print(user)
        return older_users
    
async def fetch_concurrently():
    await asyncio.gather(
        async_fetch_users(),
        async_fetch_older_users()
    )
if __name__ == "__main__":
    asyncio.run(fetch_concurrently())