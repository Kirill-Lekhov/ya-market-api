from ya_market_api.base.dataclass import BaseRequest, Region, Paging

from typing import Optional, List

from pydantic.main import BaseModel
from pydantic.fields import Field


class Request(BaseRequest):
	QUERY_PARAMS = frozenset({"name", "limit", "page_token"})

	name: str
	limit: Optional[int] = None
	page_token: Optional[str] = Field(default=None, serialization_alias="pageToken")


class Response(BaseModel):
	regions: List[Region]
	paging: Optional[Paging] = None
