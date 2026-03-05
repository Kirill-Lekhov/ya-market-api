from typing import Optional

from pydantic.main import BaseModel
from pydantic.fields import Field


class Paging(BaseModel):
	next_page_token: Optional[str] = Field(default=None, validation_alias="nextPageToken")
