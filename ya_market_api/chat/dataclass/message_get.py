from ya_market_api.base.dataclass import BaseResponse
from ya_market_api.chat.dataclass.generic import ChatMessage

from pydantic.main import BaseModel
from pydantic.fields import Field


class Request(BaseModel):
	chat_id: int = Field(ge=1, serialization_alias="chatId")
	message_id: int = Field(ge=1, serialization_alias="messageId")


class Response(BaseResponse):
	result: ChatMessage
