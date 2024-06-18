import aiohttp
import asyncio

async def main():
    async with aiohttp.ClientSession() as session:
        async with session.get('http://localhost:8080/hello') as response:
            print(await response.text())

asyncio.run(main())
