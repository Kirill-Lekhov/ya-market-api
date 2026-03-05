from ya_market_api.base.async_api_mixin import AsyncAPIMixin
from ya_market_api.chat.base_api import BaseChatAPI
from ya_market_api.chat.dataclass import (
	ChatListRequest, ChatListResponse, ChatGetRequest, ChatGetResponse, ChatMessageListRequest, ChatMessageListResponse,
	ChatMessageGetRequest, ChatMessageGetResponse, ChatMessageCreateTextRequest, ChatMessageCreateTextResponse,
	ChatMessageCreateFileRequest, ChatMessageCreateFileResponse,
)

from typing import Optional


class AsyncChatAPI(AsyncAPIMixin, BaseChatAPI):
	async def get_chat_list(self, request: Optional[ChatListRequest] = None) -> ChatListResponse:
		request = request or ChatListRequest()

		async with self.session.post(
			url=self.router.chat_list(self.business_id),
			params=request.model_dump_request_params(),
			json=request.model_dump_request_payload(),
		) as response:
			self.validate_response(response)

			return ChatListResponse.model_validate_json(await response.text())

	async def get_chat(self, request: ChatGetRequest) -> ChatGetResponse:
		async with self.session.get(
			url=self.router.chat_get(self.business_id),
			params=request.model_dump_request_params(),
		) as response:
			self.validate_response(response)

			return ChatGetResponse.model_validate_json(await response.text())

	async def get_chat_message_list(self, request: ChatMessageListRequest) -> ChatMessageListResponse:
		async with self.session.post(
			url=self.router.chat_message_list(self.business_id),
			params=request.model_dump_request_params(),
			json=request.model_dump_request_payload(),
		) as response:
			self.validate_response(response)

			return ChatMessageListResponse.model_validate_json(await response.text())

	async def get_chat_message(self, request: ChatMessageGetRequest) -> ChatMessageGetResponse:
		async with self.session.get(
			url=self.router.chat_message_get(self.business_id),
			params=request.model_dump_request_params(),
		) as response:
			self.validate_response(response)

			return ChatMessageGetResponse.model_validate_json(await response.text())

	async def create_chat_message_text(self, request: ChatMessageCreateTextRequest) -> ChatMessageCreateTextResponse:
		async with self.session.post(
			url=self.router.chat_message_create_text(self.business_id),
			params=request.model_dump_request_params(),
			json=request.model_dump_request_payload(),
		) as response:
			self.validate_response(response)

			return ChatMessageCreateTextResponse.model_validate_json(await response.text())

	async def create_chat_message_file(self, request: ChatMessageCreateFileRequest) -> ChatMessageCreateFileResponse:
		async with self.session.post(
			url=self.router.chat_message_create_file(self.business_id),
			params=request.model_dump_request_params(),
			data=request.model_dump_request_files(),
		) as response:
			self.validate_response(response)

			return ChatMessageCreateFileResponse.model_validate_json(await response.text())
