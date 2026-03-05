from ya_market_api.base.const import Status
from ya_market_api.base.dataclass import BaseRequest

from pydantic.main import BaseModel
from pydantic.fields import Field


class Request(BaseRequest):
	id: int


class Response(BaseModel):
	status: Status = Field(default=Status.OK)
