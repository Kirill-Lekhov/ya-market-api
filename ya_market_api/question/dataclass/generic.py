from ya_market_api.question.const import AuthorType

from typing import Optional

from pydantic.main import BaseModel


class Author(BaseModel):
	name: Optional[str] = None
	type: Optional[AuthorType] = None
