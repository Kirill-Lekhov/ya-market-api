from ya_market_api.base.sync_api_mixin import SyncAPIMixin
from ya_market_api.order.base_api import BaseOrderAPI
from ya_market_api.order.dataclass import OrderGetRequest, OrderGetResponse, OrderListRequest, OrderListResponse
from ya_market_api.generic.warnings import deprecated

from typing import Optional


class SyncOrderAPI(SyncAPIMixin, BaseOrderAPI):
	@deprecated()
	def get_order(self, request: OrderGetRequest) -> OrderGetResponse:
		response = self.session.get(url=self.router.order_get(self.campaign_id, request.order_id))
		self.validate_response(response)

		return OrderGetResponse.model_validate_json(response.text)

	def get_order_list(self, request: Optional[OrderListRequest] = None) -> OrderListResponse:
		request = request or OrderListRequest()
		response = self.session.post(
			url=self.router.order_list(self.business_id),
			params=request.model_dump_request_params(),
			json=request.model_dump_request_payload(),
		)
		self.validate_response(response)

		return OrderListResponse.model_validate_json(response.text)
