from ya_market_api.chat.const import ChatContextType, ChatStatusType, ChatType, ChatContextIdentifiableType
from ya_market_api.chat.dataclass.generic import Chat
from ya_market_api.base.dataclass import BaseRequest, BaseResponse

from typing import Optional, Set, List

from pydantic.main import BaseModel
from pydantic.fields import Field


class ChatContext(BaseModel):
	id: int = Field(ge=1)
	type: ChatContextIdentifiableType

	def __hash__(self) -> int:
		return hash((self.id, self.type))


class Request(BaseRequest):
	QUERY_PARAMS = frozenset({"limit", "page_token"})

	# query params
	limit: Optional[int] = Field(default=None, ge=1, le=20)
	page_token: Optional[str] = Field(default=None, serialization_alias="pageToken")

	# payload
	contexts: Optional[Set[ChatContext]] = Field(default=None, min_length=1)
	context_types: Optional[Set[ChatContextType]] = Field(default=None, serialization_alias="contextTypes")
	statuses: Optional[Set[ChatStatusType]] = Field(default=None, min_length=1)
	types: Optional[Set[ChatType]] = Field(default=None, min_length=1)


class Paging(BaseModel):
	next_page_token: Optional[str] = Field(default=None, validation_alias="nextPageToken")


class Result(BaseModel):
	chats: List[Chat]
	paging: Optional[Paging] = None


class Response(BaseResponse):
	result: Result
