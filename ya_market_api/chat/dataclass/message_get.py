from ya_market_api.base.dataclass import BaseRequest, BaseResponse
from ya_market_api.chat.dataclass.generic import ChatMessage

from pydantic.fields import Field


class Request(BaseRequest):
	QUERY_PARAMS = frozenset({"chat_id", "message_id"})

	chat_id: int = Field(ge=1, serialization_alias="chatId")
	message_id: int = Field(ge=1, serialization_alias="messageId")


class Response(BaseResponse):
	result: ChatMessage
