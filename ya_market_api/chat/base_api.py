from ya_market_api.base.api import API
from ya_market_api.chat.router import ChatRouter
from ya_market_api.exception import BusinessIdError


class BaseChatAPI(API[ChatRouter]):
	@property
	def business_id(self) -> int:
		if self.config.business_id is None:
			raise BusinessIdError("The business_id was not specified")

		return self.config.business_id

	@staticmethod
	def make_router(base_url: str) -> ChatRouter:
		return ChatRouter(base_url)
