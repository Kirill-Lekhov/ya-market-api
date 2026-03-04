from contextlib import AbstractAsyncContextManager
from types import TracebackType
from typing import Type, Optional, Union, Literal, Dict, Any


class FakeResponse(AbstractAsyncContextManager):
	def __init__(self, text: str) -> None:
		self._text = text

	async def __aenter__(self):
		return self

	async def __aexit__(
		self,
		exc_type: Optional[Type[BaseException]],
		exc_value: Optional[BaseException],
		traceback: Optional[TracebackType],
	) -> None:
		return None

	async def text(self) -> str:
		return self._text


class FakeAsyncSession:
	last_call_method: Optional[Literal["GET", "POST"]]
	last_call_url: Optional[str]
	last_call_json: Union[None, str, dict]
	last_call_params: Optional[dict]
	last_call_data: Optional[Dict[str, Any]]

	def __init__(self, response_text: str) -> None:
		self.response = FakeResponse(response_text)
		self.last_call_method = None
		self.last_call_url = None
		self.last_call_params = None
		self.last_call_json = None
		self.last_call_data = None

	def post(
		self,
		url: str,
		json: Union[None, str, dict] = None,
		params: Optional[dict] = None,
		data: Optional[Dict[str, Any]] = None,
	) -> FakeResponse:
		self.last_call_method = "POST"
		self.last_call_url = url
		self.last_call_json = json
		self.last_call_params = params
		self.last_call_data = data
		return self.response

	def get(self, url: str, params: Optional[dict] = None) -> FakeResponse:
		self.last_call_method = "GET"
		self.last_call_url = url
		self.last_call_params = params
		return self.response
