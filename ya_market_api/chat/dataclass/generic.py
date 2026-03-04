from ya_market_api.chat.const import ChatStatusType, ChatType, ChatContextType, ChatMessageSenderType

from typing import Any, Optional, List

import arrow
from pydantic.main import BaseModel
from pydantic.fields import Field
from pydantic.config import ConfigDict
from pydantic.functional_validators import field_validator


class Customer(BaseModel):
	name: Optional[str] = Field(default=None, min_length=1)
	public_id: Optional[str] = Field(default=None, min_length=1, validation_alias="publicId")


class ChatFullContext(BaseModel):
	type: ChatContextType
	campaign_id: Optional[int] = Field(default=None, ge=1, validation_alias="campaignId")
	customer: Optional[Customer] = None
	order_id: Optional[int] = Field(default=None, validation_alias="orderId")
	return_id: Optional[int] = Field(default=None, validation_alias="returnId")


class Chat(BaseModel):
	model_config = ConfigDict(arbitrary_types_allowed=True)

	id: int = Field(ge=1, validation_alias="chatId")
	context: ChatFullContext
	created_at: arrow.Arrow = Field(validation_alias="createdAt")
	status: ChatStatusType
	type: ChatType
	updated_at: arrow.Arrow = Field(validation_alias="updatedAt")
	order_id: Optional[int] = Field(default=None, deprecated=True, validation_alias="orderId")

	@field_validator("created_at", "updated_at", mode="before")
	@classmethod
	def validate_datetimes(cls, value: Any) -> arrow.Arrow:
		return arrow.get(value)


class ChatMessagePayload(BaseModel):
	name: str
	size: int	# in bytes
	url: str = Field(min_length=1, max_length=2000)


class ChatMessage(BaseModel):
	model_config = ConfigDict(arbitrary_types_allowed=True)

	id: int = Field(ge=1, validation_alias="messageId")
	created_at: Optional[arrow.Arrow] = Field(validation_alias="createdAt")
	sender: ChatMessageSenderType
	message: Optional[str] = None
	payload: Optional[List[ChatMessagePayload]] = Field(default=None, min_length=1)

	@field_validator("created_at", mode="before")
	@classmethod
	def validate_datetimes(cls, value: Any) -> arrow.Arrow:
		return arrow.get(value)
