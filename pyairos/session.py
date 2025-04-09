import atexit
import aiohttp
import asyncio


class Session:
    verify: bool
    host: str
    token: str
    session: aiohttp.ClientSession

    def __init__(self, host: str, verify: bool, token: str = None):
        self.host = host
        self.token = token
        self.verify = verify
        self.cookie_jar = aiohttp.CookieJar(unsafe=True)
        self.session = aiohttp.ClientSession(cookie_jar=self.cookie_jar)
        atexit.register(self.cleanup)

    def cleanup(self):
        asyncio.run(self.session.close())

    async def ping(self):
        try:
            response = await self.session.get(self.host, ssl=self.verify)
            if response.status == 200:
                return True
            else:
                return False
        except aiohttp.ClientConnectionError as e:
            print(f"Ping failed: {e}")
            return False

    async def get(self, url: str):
        response = await self.session.get(self.host + url, ssl=self.verify) 
        response.raise_for_status()

        return await response.json()

    async def post(self, url: str, data: dict):
        response = await  self.session.post(
            self.host + url, data=data, ssl=self.verify
        )
        response.raise_for_status()

        return await response.json()

    def get_host(self):
        return self.host

    def set_token(self, token=None):
        self.token = token
