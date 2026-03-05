from ya_market_api.question.const import QuestionSortOrderType
from ya_market_api.question.dataclass.generic import Author
from ya_market_api.base.dataclass import BaseRequest, BaseResponse, Votes, Paging

from typing import Optional, Set, Any, List

import arrow
from pydantic.main import BaseModel
from pydantic.fields import Field
from pydantic.config import ConfigDict
from pydantic.functional_serializers import field_serializer
from pydantic.functional_validators import field_validator


class Request(BaseRequest):
	QUERY_PARAMS = frozenset({"limit", "page_token"})
	model_config = ConfigDict(arbitrary_types_allowed=True)

	# query params
	limit: Optional[int] = Field(default=None, ge=1, le=50)
	page_token: Optional[str] = Field(default=None, serialization_alias="pageToken")

	# payload
	category_ids: Optional[Set[int]] = Field(default=None, serialization_alias="categoryIds")
	date_from: Optional[arrow.Arrow] = Field(default=None, serialization_alias="dateFrom")
	date_to: Optional[arrow.Arrow] = Field(default=None, serialization_alias="dateTo")
	need_answer: Optional[bool] = Field(default=None, serialization_alias="needAnswer")
	sort: Optional[QuestionSortOrderType] = None

	@field_serializer("date_from", "date_to", mode="plain")
	def serialize_optional_dates(self, value: Optional[arrow.Arrow]) -> Optional[str]:
		if value is None:
			return None

		return value.date().isoformat()


class QuestionIdentifiers(BaseModel):
	id: int = Field(ge=1)
	offer_id: str = Field(min_length=1, max_length=255, validation_alias="offerId")
	category_id: Optional[int] = Field(ge=0, validation_alias="categoryId")


class Question(BaseModel):
	model_config = ConfigDict(arbitrary_types_allowed=True)

	author: Author
	business_id: int = Field(ge=1, validation_alias="businessId")
	created_at: arrow.Arrow = Field(validation_alias="createdAt")
	question_ids: QuestionIdentifiers = Field(validation_alias="questionIdentifiers")
	text: str = Field(min_length=1, max_length=5000)
	votes: Votes

	@field_validator("created_at", mode="before")
	@classmethod
	def validate_datetimes(cls, value: Any) -> arrow.Arrow:
		return arrow.get(value)


class Result(BaseModel):
	questions: List[Question]
	total_count: int = Field(validation_alias="totalCount")
	paging: Optional[Paging] = None


class Response(BaseResponse):
	result: Result
