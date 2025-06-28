from ya_market_api.base.router import Router
from ya_market_api.const import BASE_URL

from functools import cache


class GuideRegionRouter(Router):
	@cache
	def region_countries(self) -> str:
		return f"{BASE_URL}/regions/countries"

	@cache
	def region_search(self) -> str:
		return f"{BASE_URL}/regions"

	def region_info(self, region_id: int) -> str:
		return f"{BASE_URL}/regions/{region_id}"

	def region_children(self, region_id: int) -> str:
		return f"{BASE_URL}/regions/{region_id}/children"
