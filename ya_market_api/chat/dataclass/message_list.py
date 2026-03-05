from ya_market_api.base.dataclass import BaseRequest, BaseResponse
from ya_market_api.chat.dataclass.generic import ChatFullContext, ChatMessage

from typing import Optional, List

from pydantic.main import BaseModel
from pydantic.fields import Field


class Request(BaseRequest):
	QUERY_PARAMS = frozenset({"chat_id", "limit", "page_token"})

	# query params
	chat_id: int = Field(ge=1, serialization_alias="chatId")
	limit: Optional[int] = Field(default=None, ge=1, le=100)
	page_token: Optional[str] = Field(default=None, serialization_alias="pageToken")

	# payload
	message_id_from: Optional[int] = Field(default=None, serialization_alias="messageIdFrom")


class Paging(BaseModel):
	next_page_token: Optional[str] = Field(default=None, validation_alias="nextPageToken")


class Result(BaseModel):
	context: ChatFullContext
	messages: List[ChatMessage]
	paging: Optional[Paging] = None


class Response(BaseResponse):
	result: Result
