from ya_market_api.base.sync_api_mixin import SyncAPIMixin
from ya_market_api.guide.region.base_api import BaseGuideRegionAPI
from ya_market_api.guide.region.dataclass import (
	RegionCountriesResponse, RegionSearchRequest, RegionSearchResponse, RegionInfoRequest, RegionInfoResponse,
	RegionChildrenRequest, RegionChildrenResponse,
)


class SyncGuideRegionAPI(SyncAPIMixin, BaseGuideRegionAPI):
	def get_region_countries(self) -> RegionCountriesResponse:
		response = self.session.post(url=self.router.region_countries(), json="")
		self.validate_response(response)

		return RegionCountriesResponse.model_validate_json(response.text)

	def search_region(self, request: RegionSearchRequest) -> RegionSearchResponse:
		response = self.session.get(
			url=self.router.region_search(),
			params=request.model_dump_request_params(),
		)
		self.validate_response(response)

		return RegionSearchResponse.model_validate_json(response.text)

	def get_region_info(self, request: RegionInfoRequest) -> RegionInfoResponse:
		response = self.session.get(url=self.router.region_info(request.region_id))
		self.validate_response(response)

		return RegionInfoResponse.model_validate_json(response.text)

	def get_region_children(self, request: RegionChildrenRequest) -> RegionChildrenResponse:
		response = self.session.get(
			url=self.router.region_children(request.region_id),
			params=request.model_dump_request_params(),
		)
		self.validate_response(response)

		return RegionChildrenResponse.model_validate_json(response.text)
