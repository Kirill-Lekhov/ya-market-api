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
		url = self.router.chat_list(self.business_id)
		response = self.session.post(
			url=url,
			params=request.model_dump_request_params(),
			json=request.model_dump_request_payload(),
		)
		self.validate_response(response)

		return ChatListResponse.model_validate_json(response.text)

	def get_chat(self, request: ChatGetRequest) -> ChatGetResponse:
		url = self.router.chat_get(self.business_id)
		response = self.session.get(url=url, params=request.model_dump(by_alias=True))
		self.validate_response(response)

		return ChatGetResponse.model_validate_json(response.text)

	def get_chat_message_list(self, request: ChatMessageListRequest) -> ChatMessageListResponse:
		url = self.router.chat_message_list(self.business_id)
		response = self.session.post(
			url=url,
			params=request.model_dump_request_params(),
			json=request.model_dump_request_payload(),
		)
		self.validate_response(response)

		return ChatMessageListResponse.model_validate_json(response.text)

	def get_chat_message(self, request: ChatMessageGetRequest) -> ChatMessageGetResponse:
		url = self.router.chat_message_get(self.business_id)
		response = self.session.get(url=url, params=request.model_dump(by_alias=True))
		self.validate_response(response)

		return ChatMessageGetResponse.model_validate_json(response.text)

	def create_chat_message_text(self, request: ChatMessageCreateTextRequest) -> ChatMessageCreateTextResponse:
		url = self.router.chat_message_create_text(self.business_id)
		response = self.session.post(
			url=url,
			params=request.model_dump_request_params(),
			json=request.model_dump_request_payload(),
		)
		self.validate_response(response)

		return ChatMessageCreateTextResponse.model_validate_json(response.text)

	def create_chat_message_file(self, request: ChatMessageCreateFileRequest) -> ChatMessageCreateFileResponse:
		url = self.router.chat_message_create_file(self.business_id)
		response = self.session.post(
			url=url,
			params=request.model_dump_request_params(),
			files=request.model_dump_request_payload(),
		)
		self.validate_response(response)

		return ChatMessageCreateFileResponse.model_validate_json(response.text)
