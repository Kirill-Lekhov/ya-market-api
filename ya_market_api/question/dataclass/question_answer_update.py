from pydantic.main import BaseModel
from pydantic.fields import Field


class Request(BaseModel):
	answer_id: int
	text: str = Field(min_length=1, max_length=5000)


class Response(BaseModel):
	pass
