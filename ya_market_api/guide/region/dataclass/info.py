from ya_market_api.base.dataclass import BaseRequest, Region, Paging

from typing import List, Optional

from pydantic.main import BaseModel


class Request(BaseRequest):
	PATH_PARAMS = frozenset({"region_id"})

	region_id: int


class Response(BaseModel):
	regions: List[Region]
	paging: Optional[Paging] = None
