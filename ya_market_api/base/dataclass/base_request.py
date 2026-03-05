from typing import Dict, Any, ClassVar, FrozenSet

from pydantic.main import BaseModel


class BaseRequest(BaseModel):
	QUERY_PARAMS: ClassVar[FrozenSet[str]] = frozenset()
	FILES: ClassVar[FrozenSet[str]] = frozenset()
	PATH_PARAMS: ClassVar[FrozenSet[str]] = frozenset()

	def model_dump_request_params(self) -> Dict[str, Any]:
		return self.model_dump(include=self.QUERY_PARAMS, by_alias=True, exclude_none=True, mode="json")

	def model_dump_request_files(self) -> Dict[str, bytes]:
		return self.model_dump(include=self.FILES, by_alias=True, exclude_none=True)

	def model_dump_request_payload(self) -> Dict[str, Any]:
		return self.model_dump(
			exclude=self.QUERY_PARAMS | self.FILES | self.PATH_PARAMS,
			by_alias=True,
			exclude_none=True,
			mode="json",
		)
