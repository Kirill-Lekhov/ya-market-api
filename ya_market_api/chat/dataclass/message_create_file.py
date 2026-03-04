from ya_market_api.base.const import Status

from typing import ClassVar, FrozenSet, Dict, Any

from pydantic.main import BaseModel
from pydantic.fields import Field


class Request(BaseModel):
	QUERY_PARAMS: ClassVar[FrozenSet[str]] = frozenset({"chat_id"})

	# query params
	chat_id: int = Field(ge=1, serialization_alias="chatId")

	# payload
	file: bytes = Field(max_length=5_000_000)		# 5 mb

	def model_dump_request_params(self) -> Dict[str, Any]:
		return self.model_dump(include=self.QUERY_PARAMS, by_alias=True)

	def model_dump_request_payload(self) -> Dict[str, Any]:
		return self.model_dump(exclude=self.QUERY_PARAMS, by_alias=True)


class Response(BaseModel):
	status: Status = Field(default=Status.OK)
