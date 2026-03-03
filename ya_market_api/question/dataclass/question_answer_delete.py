from pydantic.main import BaseModel


class Request(BaseModel):
	answer_id: int


class Response(BaseModel):
	pass
