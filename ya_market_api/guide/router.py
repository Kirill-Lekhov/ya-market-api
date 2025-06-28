from ya_market_api.base.router import Router
from ya_market_api.const import BASE_URL

from functools import cache


class GuideRouter(Router):
	@cache
	def token_info(self) -> str:
		return f"{BASE_URL}/auth/token"

	@cache
	def delivery_services(self) -> str:
		return f"{BASE_URL}/delivery/services"
