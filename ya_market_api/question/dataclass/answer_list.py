from ya_market_api.base.dataclass import BaseRequest, BaseResponse, Votes
from ya_market_api.question.const import ModerationStatus
from ya_market_api.question.dataclass.generic import Author

from typing import Optional, Any, List

import arrow
from pydantic.main import BaseModel
from pydantic.fields import Field
from pydantic.config import ConfigDict
from pydantic.functional_validators import field_validator


class Request(BaseRequest):
	QUERY_PARAMS = frozenset({"limit", "page_token"})

	# query params
	limit: Optional[int] = None
	page_token: Optional[str] = Field(default=None, serialization_alias="pageToken")

	# payload
	question_id: int = Field(serialization_alias="questionId")


class Comment(BaseModel):
	model_config = ConfigDict(arbitrary_types_allowed=True)

	answer_id: int = Field(ge=1, validation_alias="answerId")
	created_at: arrow.Arrow = Field(validation_alias="createdAt")
	id: int = Field(ge=1)
	status: ModerationStatus
	text: str = Field(max_length=5000)
	author: Optional[Author] = None
	can_modify: Optional[bool] = Field(default=None, validation_alias="canModify")
	parent_id: Optional[int] = Field(default=None, ge=1, validation_alias="parentId")
	votes: Optional[Votes] = None

	@field_validator("created_at", mode="before")
	@classmethod
	def validate_datetimes(cls, value: Any) -> arrow.Arrow:
		return arrow.get(value)


class Answer(BaseModel):
	model_config = ConfigDict(arbitrary_types_allowed=True)

	can_modify: bool = Field(validation_alias="canModify")
	created_at: arrow.Arrow = Field(validation_alias="createdAt")
	id: int = Field(ge=1)
	question_id: int = Field(ge=1, validation_alias="questionId")
	status: ModerationStatus
	text: str = Field(min_length=1, max_length=5000)
	votes: Votes
	author: Optional[Author] = None
	comments: Optional[List[Comment]] = Field(default=None, max_length=100)

	@field_validator("created_at", mode="before")
	@classmethod
	def validate_datetimes(cls, value: Any) -> arrow.Arrow:
		return arrow.get(value)


class Paging(BaseModel):
	next_page_token: Optional[str] = Field(default=None, validation_alias="nextPageToken")


class Result(BaseModel):
	answers: List[Answer]
	paging: Optional[Paging] = None


class Response(BaseResponse):
	result: Result
