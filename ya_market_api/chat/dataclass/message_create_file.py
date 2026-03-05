from ya_market_api.base.const import Status
from ya_market_api.base.dataclass import BaseRequest

from pydantic.main import BaseModel
from pydantic.fields import Field


class Request(BaseRequest):
	QUERY_PARAMS = frozenset({"chat_id"})
	FILES = frozenset({"file"})

	# query params
	chat_id: int = Field(ge=1, serialization_alias="chatId")

	# payload
	file: bytes = Field(max_length=5_000_000)		# 5 mb


class Response(BaseModel):
	status: Status = Field(default=Status.OK)
