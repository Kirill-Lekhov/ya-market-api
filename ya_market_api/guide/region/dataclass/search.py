from ya_market_api.base.dataclass import BaseRequest, Region

from typing import Optional, List

from pydantic.main import BaseModel
from pydantic.fields import Field


class Request(BaseRequest):
	QUERY_PARAMS = frozenset({"name", "limit", "page_token"})

	name: str
	limit: Optional[int] = None
	page_token: Optional[str] = Field(default=None, serialization_alias="pageToken")


class ResponsePaging(BaseModel):
	next_page_token: Optional[str] = Field(default=None, validation_alias="nextPageToken")


class Response(BaseModel):
	regions: List[Region]
	paging: Optional[ResponsePaging] = None
