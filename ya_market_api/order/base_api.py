from ya_market_api.base.api import API
from ya_market_api.exception import CampaignIdError, BusinessIdError
from ya_market_api.order.router import OrderRouter


class BaseOrderAPI(API[OrderRouter]):
	@property
	def campaign_id(self) -> int:
		if self.config.campaign_id is None:
			raise CampaignIdError("The campaign_id was not specified")

		return self.config.campaign_id

	@property
	def business_id(self) -> int:
		if self.config.business_id is None:
			raise BusinessIdError("The business_id was not specified")

		return self.config.business_id

	@staticmethod
	def make_router(base_url: str) -> OrderRouter:
		return OrderRouter(base_url)
