from ya_market_api.base.async_api_mixin import AsyncAPIMixin
from ya_market_api.guide.region.base_api import BaseGuideRegionAPI
from ya_market_api.guide.region.dataclass import (
	RegionCountriesResponse, RegionSearchRequest, RegionSearchResponse, RegionInfoRequest, RegionInfoResponse,
	RegionChildrenRequest, RegionChildrenResponse,
)


class AsyncGuideRegionAPI(AsyncAPIMixin, BaseGuideRegionAPI):
	async def get_region_countries(self) -> RegionCountriesResponse:
		async with self.session.post(url=self.router.region_countries(), json="") as response:
			self.validate_response(response)

			return RegionCountriesResponse.model_validate_json(await response.text())

	async def search_region(self, request: RegionSearchRequest) -> RegionSearchResponse:
		async with self.session.get(
			url=self.router.region_search(),
			params=request.model_dump_request_params(),
		) as response:
			self.validate_response(response)

			return RegionSearchResponse.model_validate_json(await response.text())

	async def get_region_info(self, request: RegionInfoRequest) -> RegionInfoResponse:
		async with self.session.get(url=self.router.region_info(request.region_id)) as response:
			self.validate_response(response)

			return RegionInfoResponse.model_validate_json(await response.text())

	async def get_region_children(self, request: RegionChildrenRequest) -> RegionChildrenResponse:
		async with self.session.get(
			url=self.router.region_children(request.region_id),
			params=request.model_dump_request_params(),
		) as response:
			self.validate_response(response)

			return RegionChildrenResponse.model_validate_json(await response.text())
