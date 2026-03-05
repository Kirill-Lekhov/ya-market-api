from ya_market_api.base.dataclass import BaseRequest, BaseResponse
from ya_market_api.chat.dataclass.generic import Chat

from pydantic.fields import Field


class Request(BaseRequest):
	QUERY_PARAMS = frozenset({"chat_id"})

	chat_id: int = Field(serialization_alias="chatId")


class Response(BaseResponse):
	result: Chat
