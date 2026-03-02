from ya_market_api.base.router import Router


class OrderRouter(Router):
	def order_get(self, campaign_id: int, order_id: int) -> str:
		return f"{self.base_url}/campaigns/{campaign_id}/orders/{order_id}"

	def order_list(self, business_id: int) -> str:
		return f"{self.base_url}/v1/businesses/{business_id}/orders"
