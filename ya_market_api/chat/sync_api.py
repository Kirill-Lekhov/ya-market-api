from ya_market_api.base.sync_api_mixin import SyncAPIMixin
from ya_market_api.chat.base_api import BaseChatAPI
from ya_market_api.chat.dataclass import (
	ChatListRequest, ChatListResponse, ChatGetRequest, ChatGetResponse, ChatMessageListRequest, ChatMessageListResponse,
	ChatMessageGetRequest, ChatMessageGetResponse, ChatMessageCreateTextRequest, ChatMessageCreateTextResponse,
	ChatMessageCreateFileRequest, ChatMessageCreateFileResponse,
)

from typing import Optional


class SyncChatAPI(SyncAPIMixin, BaseChatAPI):
	def get_chat_list(self, request: Optional[ChatListRequest] = None) -> ChatListResponse:
		request = request or ChatListRequest()
		response = self.session.post(
			url=self.router.chat_list(self.business_id),
			params=request.model_dump_request_params(),
			json=request.model_dump_request_payload(),
		)
		self.validate_response(response)

		return ChatListResponse.model_validate_json(response.text)

	def get_chat(self, request: ChatGetRequest) -> ChatGetResponse:
		response = self.session.get(
			url=self.router.chat_get(self.business_id),
			params=request.model_dump_request_params(),
		)
		self.validate_response(response)

		return ChatGetResponse.model_validate_json(response.text)

	def get_chat_message_list(self, request: ChatMessageListRequest) -> ChatMessageListResponse:
		response = self.session.post(
			url=self.router.chat_message_list(self.business_id),
			params=request.model_dump_request_params(),
			json=request.model_dump_request_payload(),
		)
		self.validate_response(response)

		return ChatMessageListResponse.model_validate_json(response.text)

	def get_chat_message(self, request: ChatMessageGetRequest) -> ChatMessageGetResponse:
		response = self.session.get(
			url=self.router.chat_message_get(self.business_id),
			params=request.model_dump_request_params(),
		)
		self.validate_response(response)

		return ChatMessageGetResponse.model_validate_json(response.text)

	def create_chat_message_text(self, request: ChatMessageCreateTextRequest) -> ChatMessageCreateTextResponse:
		response = self.session.post(
			url=self.router.chat_message_create_text(self.business_id),
			params=request.model_dump_request_params(),
			json=request.model_dump_request_payload(),
		)
		self.validate_response(response)

		return ChatMessageCreateTextResponse.model_validate_json(response.text)

	def create_chat_message_file(self, request: ChatMessageCreateFileRequest) -> ChatMessageCreateFileResponse:
		response = self.session.post(
			url=self.router.chat_message_create_file(self.business_id),
			params=request.model_dump_request_params(),
			files=request.model_dump_request_files(),
		)
		self.validate_response(response)

		return ChatMessageCreateFileResponse.model_validate_json(response.text)
