from ya_market_api.const import Header
from ya_market_api.guide.async_api import AsyncGuideAPI

from aiohttp.client import ClientSession


class AsyncAPI:
	guide: AsyncGuideAPI
	session: ClientSession

	def __init__(self, session: ClientSession) -> None:
		self.session = session
		self.guide = AsyncGuideAPI(session)

	@classmethod
	async def build(cls, api_key: str) -> "AsyncAPI":
		session = await cls.make_session(api_key)

		return cls(session)

	@staticmethod
	async def make_session(api_key: str) -> ClientSession:
		session = ClientSession(headers={Header.API_KEY.value: api_key})
		return session
