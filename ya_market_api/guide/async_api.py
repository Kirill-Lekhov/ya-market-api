from ya_market_api.base.async_api_mixin import AsyncAPIMixin
from ya_market_api.base.async_config import AsyncConfig
from ya_market_api.guide.base_api import BaseGuideAPI
from ya_market_api.guide.dataclass import TokenInfoResponse, DeliveryServicesResponse
from ya_market_api.guide.region.async_api import AsyncGuideRegionAPI


class AsyncGuideAPI(AsyncAPIMixin, BaseGuideAPI):
	def __init__(self, config: AsyncConfig) -> None:
		super().__init__(config)
		self.region = AsyncGuideRegionAPI(config)

	async def get_token_info(self) -> TokenInfoResponse:
		async with self.session.post(url=self.router.token_info(), json="") as response:
			self.validate_response(response)

			return TokenInfoResponse.model_validate_json(await response.text())

	async def get_delivery_services(self) -> DeliveryServicesResponse:
		async with self.session.get(url=self.router.delivery_services()) as response:
			self.validate_response(response)

			return DeliveryServicesResponse.model_validate_json(await response.text())
