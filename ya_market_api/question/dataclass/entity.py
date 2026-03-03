from ya_market_api.base.dataclass import BaseResponse
from ya_market_api.question.const import EntityOperationType, EntityType

from typing import Optional, Dict, Any, Literal, overload

from pydantic.main import BaseModel
from pydantic.fields import Field


class EntityId(BaseModel):
	id: int
	type: EntityType


class EntityRequest(BaseModel):
	operation_type: EntityOperationType = Field(serialization_alias="operationType")
	entity_id: Optional[EntityId] = Field(default=None, serialization_alias="entityId")
	parent_entity_id: Optional[EntityId] = Field(default=None, serialization_alias="parentEntityId")
	text: Optional[str] = Field(default=None, min_length=1, max_length=5000)

	@overload
	def __init__(
		self,
		*,
		operation_type: Literal[EntityOperationType.CREATE],
		parent_entity_id: EntityId,
		text: str,
	) -> None: ...

	@overload
	def __init__(
		self,
		*,
		operation_type: Literal[EntityOperationType.UPDATE],
		entity_id: EntityId,
		text: str,
	) -> None: ...

	@overload
	def __init__(self, *, operation_type: Literal[EntityOperationType.DELETE], entity_id: EntityId) -> None: ...

	def __init__(
		self,
		*,
		operation_type: EntityOperationType,
		entity_id: Optional[EntityId] = None,
		parent_entity_id: Optional[EntityId] = None,
		text: Optional[str] = None,
	) -> None:
		super().__init__(
			operation_type=operation_type,
			entity_id=entity_id,
			parent_entity_id=parent_entity_id,
			text=text,
		)

	def model_dump_request_payload(self) -> Dict[str, Any]:
		return self.model_dump(by_alias=True, exclude_none=True, mode="json")


class EntityCreateResult(BaseModel):
	entity: EntityId


class EntityCreateResponse(BaseResponse):
	result: EntityCreateResult
