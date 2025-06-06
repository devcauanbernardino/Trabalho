import asyncio
from database import engine

async def test_connection():
    async with engine.connect() as conn:
        print("✅ Conexão com o banco estabelecida com sucesso!")
        await conn.close()

if __name__ == "__main__":
    asyncio.run(test_connection())