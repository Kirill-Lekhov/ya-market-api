from ya_market_api.base.dataclass import BaseResponse
from ya_market_api.chat.dataclass.generic import ChatFullContext, ChatMessage

from typing import ClassVar, FrozenSet, Optional, Dict, Any, List

from pydantic.main import BaseModel
from pydantic.fields import Field


class Request(BaseModel):
	QUERY_PARAMS: ClassVar[FrozenSet[str]] = frozenset({"chat_id", "limit", "page_token"})

	# query params
	chat_id: int = Field(ge=1, serialization_alias="chatId")
	limit: Optional[int] = Field(default=None, ge=1, le=100)
	page_token: Optional[str] = Field(default=None, serialization_alias="pageToken")

	# payload
	message_id_from: Optional[int] = Field(default=None, serialization_alias="messageIdFrom")

	def model_dump_request_params(self) -> Dict[str, Any]:
		return self.model_dump(include=self.QUERY_PARAMS, by_alias=True, exclude_none=True)

	def model_dump_request_payload(self) -> Dict[str, Any]:
		return self.model_dump(exclude=self.QUERY_PARAMS, by_alias=True, exclude_none=True)


class Paging(BaseModel):
	next_page_token: Optional[str] = Field(default=None, validation_alias="nextPageToken")


class Result(BaseModel):
	context: ChatFullContext
	messages: List[ChatMessage]
	paging: Optional[Paging] = None


class Response(BaseResponse):
	result: Result
