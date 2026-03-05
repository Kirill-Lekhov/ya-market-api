from ya_market_api.base.async_api_mixin import AsyncAPIMixin
from ya_market_api.order.base_api import BaseOrderAPI
from ya_market_api.order.dataclass import OrderGetRequest, OrderGetResponse, OrderListRequest, OrderListResponse
from ya_market_api.generic.warnings import deprecated

from typing import Optional


class AsyncOrderAPI(AsyncAPIMixin, BaseOrderAPI):
	@deprecated()
	async def get_order(self, request: OrderGetRequest) -> OrderGetResponse:
		async with self.session.get(url=self.router.order_get(self.campaign_id, request.order_id)) as response:
			self.validate_response(response)

			return OrderGetResponse.model_validate_json(await response.text())

	async def get_order_list(self, request: Optional[OrderListRequest] = None) -> OrderListResponse:
		request = request or OrderListRequest()

		async with self.session.post(
			url=self.router.order_list(self.business_id),
			params=request.model_dump_request_params(),
			json=request.model_dump_request_payload(),
		) as response:
			self.validate_response(response)

			return OrderListResponse.model_validate_json(await response.text())
