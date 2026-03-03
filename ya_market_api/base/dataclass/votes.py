from pydantic.main import BaseModel


class Votes(BaseModel):
	dislikes: int
	likes: int
