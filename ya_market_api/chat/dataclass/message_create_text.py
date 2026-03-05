from ya_market_api.base.const import Status
from ya_market_api.base.dataclass import BaseRequest

from pydantic.main import BaseModel
from pydantic.fields import Field


class Request(BaseRequest):
	QUERY_PARAMS = frozenset({"chat_id"})

	# query params
	chat_id: int = Field(ge=1, serialization_alias="chatId")

	# payload
	message: str = Field(min_length=1, max_length=4096)


class Response(BaseModel):
	status: Status = Field(default=Status.OK)
