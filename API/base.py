import aiohttp

class BaseApi:
    async def get(self, url):
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as reques:
                answer = await reques.json()
                return answer
