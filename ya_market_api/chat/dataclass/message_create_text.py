from ya_market_api.base.const import Status

from typing import Dict, Any, ClassVar, FrozenSet

from pydantic.main import BaseModel
from pydantic.fields import Field


class Request(BaseModel):
	QUERY_PARAMS: ClassVar[FrozenSet[str]] = frozenset({"chat_id"})

	# query params
	chat_id: int = Field(ge=1, serialization_alias="chatId")

	# payload
	message: str = Field(min_length=1, max_length=4096)

	def model_dump_request_params(self) -> Dict[str, Any]:
		return self.model_dump(include=self.QUERY_PARAMS, by_alias=True)

	def model_dump_request_payload(self) -> Dict[str, Any]:
		return self.model_dump(exclude=self.QUERY_PARAMS, by_alias=True)


class Response(BaseModel):
	status: Status = Field(default=Status.OK)
