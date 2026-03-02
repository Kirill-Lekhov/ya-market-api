from ya_market_api.base.sync_api_mixin import SyncAPIMixin
from ya_market_api.order.base_api import BaseOrderAPI
from ya_market_api.order.dataclass import OrderGetRequest, OrderGetResponse, OrderListRequest, OrderListResponse
from ya_market_api.generic.warnings import deprecated

from typing import Optional


class SyncOrderAPI(SyncAPIMixin, BaseOrderAPI):
	@deprecated()
	def get_order(self, request: OrderGetRequest) -> OrderGetResponse:
		url = self.router.order_get(self.campaign_id, request.order_id)
		response = self.session.get(url=url)
		self.validate_response(response)
		return OrderGetResponse.model_validate_json(response.text)

	def get_order_list(self, request: Optional[OrderListRequest] = None) -> OrderListResponse:
		request = request or OrderListRequest()
		url = self.router.order_list(self.business_id)
		response = self.session.post(
			url=url,
			params=request.model_dump_request_params(),
			json=request.model_dump_request_payload(),
		)
		self.validate_response(response)
		return OrderListResponse.model_validate_json(response.text)
