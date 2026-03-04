from ya_market_api.base.dataclass import BaseResponse
from ya_market_api.chat.dataclass.generic import Chat

from pydantic.main import BaseModel
from pydantic.fields import Field


class Request(BaseModel):
	chat_id: int = Field(serialization_alias="chatId")


class Response(BaseResponse):
	result: Chat
