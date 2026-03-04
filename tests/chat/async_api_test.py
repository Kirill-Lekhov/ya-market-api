from tests.fake_async_session import FakeAsyncSession
from ya_market_api.chat.async_api import AsyncChatAPI
from ya_market_api.chat.dataclass import (
	ChatListRequest, ChatGetRequest, ChatMessageListRequest, ChatMessageGetRequest, ChatMessageCreateTextRequest,
	ChatMessageCreateFileRequest,
)
from ya_market_api.chat.const import ChatType
from ya_market_api.base.async_config import AsyncConfig

from unittest.mock import patch

import pytest


class TestAsyncChatAPI:
	@pytest.mark.asyncio()
	async def test_get_chat_list(self):
		session = FakeAsyncSession("RAW DATA")
		config = AsyncConfig(session, "", business_id=1)		# type: ignore - for testing purposes
		api = AsyncChatAPI(config)
		request = ChatListRequest(limit=20, page_token="PAGE TOKEN", types={ChatType.CHAT})

		with patch("ya_market_api.chat.async_api.ChatListResponse") as ChatListResponseMock:
			ChatListResponseMock.model_validate_json.return_value = "DESERIALIZED DATA"

			with patch.object(api, "validate_response") as validate_response_mock:
				assert await api.get_chat_list() == "DESERIALIZED DATA"
				ChatListResponseMock.model_validate_json.assert_called_once_with("RAW DATA")
				validate_response_mock.assert_called_once_with(session.response)
				assert session.last_call_method == "POST"
				assert session.last_call_url == api.router.chat_list(1)
				assert session.last_call_json == {}
				assert session.last_call_params == {}

				assert await api.get_chat_list(request) == "DESERIALIZED DATA"
				assert session.last_call_method == "POST"
				assert session.last_call_url == api.router.chat_list(1)
				assert session.last_call_json == {"types": [ChatType.CHAT.value]}
				assert session.last_call_params == {"limit": 20, "pageToken": "PAGE TOKEN"}

	@pytest.mark.asyncio()
	async def test_get_chat(self):
		session = FakeAsyncSession("RAW DATA")
		config = AsyncConfig(session, "", business_id=1)		# type: ignore - for testing purposes
		api = AsyncChatAPI(config)
		request = ChatGetRequest(chat_id=512)

		with patch("ya_market_api.chat.async_api.ChatGetResponse") as ChatGetResponseMock:
			ChatGetResponseMock.model_validate_json.return_value = "DESERIALIZED DATA"

			with patch.object(api, "validate_response") as validate_response_mock:
				assert await api.get_chat(request) == "DESERIALIZED DATA"
				ChatGetResponseMock.model_validate_json.assert_called_once_with("RAW DATA")
				validate_response_mock.assert_called_once_with(session.response)
				assert session.last_call_method == "GET"
				assert session.last_call_url == api.router.chat_get(1)
				assert session.last_call_json is None
				assert session.last_call_params == {"chatId": 512}

	@pytest.mark.asyncio()
	async def test_get_chat_message_list(self):
		session = FakeAsyncSession("RAW DATA")
		config = AsyncConfig(session, "", business_id=1)		# type: ignore - for testing purposes
		api = AsyncChatAPI(config)
		request = ChatMessageListRequest(chat_id=512)

		with patch("ya_market_api.chat.async_api.ChatMessageListResponse") as ChatMessageListResponseMock:
			ChatMessageListResponseMock.model_validate_json.return_value = "DESERIALIZED DATA"

			with patch.object(api, "validate_response") as validate_response_mock:
				assert await api.get_chat_message_list(request) == "DESERIALIZED DATA"
				ChatMessageListResponseMock.model_validate_json.assert_called_once_with("RAW DATA")
				validate_response_mock.assert_called_once_with(session.response)
				assert session.last_call_method == "POST"
				assert session.last_call_url == api.router.chat_message_list(1)
				assert session.last_call_json == {}
				assert session.last_call_params == {"chatId": 512}

				request = ChatMessageListRequest(chat_id=512, limit=10, page_token="PAGE TOKEN", message_id_from=1024)
				assert await api.get_chat_message_list(request) == "DESERIALIZED DATA"
				assert session.last_call_method == "POST"
				assert session.last_call_url == api.router.chat_message_list(1)
				assert session.last_call_json == {"messageIdFrom": 1024}
				assert session.last_call_params == {"chatId": 512, "limit": 10, "pageToken": "PAGE TOKEN"}

	@pytest.mark.asyncio()
	async def test_get_chat_message(self):
		session = FakeAsyncSession("RAW DATA")
		config = AsyncConfig(session, "", business_id=1)		# type: ignore - for testing purposes
		api = AsyncChatAPI(config)
		request = ChatMessageGetRequest(chat_id=512, message_id=1024)

		with patch("ya_market_api.chat.async_api.ChatMessageGetResponse") as ChatMessageGetResponseMock:
			ChatMessageGetResponseMock.model_validate_json.return_value = "DESERIALIZED DATA"

			with patch.object(api, "validate_response") as validate_response_mock:
				assert await api.get_chat_message(request) == "DESERIALIZED DATA"
				ChatMessageGetResponseMock.model_validate_json.assert_called_once_with("RAW DATA")
				validate_response_mock.assert_called_once_with(session.response)
				assert session.last_call_method == "GET"
				assert session.last_call_url == api.router.chat_message_get(1)
				assert session.last_call_json == None
				assert session.last_call_params == {"chatId": 512, "messageId": 1024}

	@pytest.mark.asyncio()
	async def test_create_chat_message_text(self):
		session = FakeAsyncSession("RAW DATA")
		config = AsyncConfig(session, "", business_id=1)		# type: ignore - for testing purposes
		api = AsyncChatAPI(config)
		request = ChatMessageCreateTextRequest(chat_id=512, message="HELLO WORLD")

		with patch("ya_market_api.chat.async_api.ChatMessageCreateTextResponse") as ChatMessageCreateTextResponseMock:
			ChatMessageCreateTextResponseMock.model_validate_json.return_value = "DESERIALIZED DATA"

			with patch.object(api, "validate_response") as validate_response_mock:
				assert await api.create_chat_message_text(request) == "DESERIALIZED DATA"
				ChatMessageCreateTextResponseMock.model_validate_json.assert_called_once_with("RAW DATA")
				validate_response_mock.assert_called_once_with(session.response)
				assert session.last_call_method == "POST"
				assert session.last_call_url == api.router.chat_message_create_text(1)
				assert session.last_call_json == {"message": "HELLO WORLD"}
				assert session.last_call_params == {"chatId": 512}

	@pytest.mark.asyncio()
	async def test_create_chat_message_file(self):
		session = FakeAsyncSession("RAW DATA")
		config = AsyncConfig(session, "", business_id=1)		# type: ignore - for testing purposes
		api = AsyncChatAPI(config)
		request = ChatMessageCreateFileRequest(chat_id=512, file=b"HELLO WORLD")

		with patch("ya_market_api.chat.async_api.ChatMessageCreateFileResponse") as ChatMessageCreateFileResponseMock:
			ChatMessageCreateFileResponseMock.model_validate_json.return_value = "DESERIALIZED DATA"

			with patch.object(api, "validate_response") as validate_response_mock:
				assert await api.create_chat_message_file(request) == "DESERIALIZED DATA"
				ChatMessageCreateFileResponseMock.model_validate_json.assert_called_once_with("RAW DATA")
				validate_response_mock.assert_called_once_with(session.response)
				assert session.last_call_method == "POST"
				assert session.last_call_url == api.router.chat_message_create_file(1)
				assert session.last_call_data == {"file": b"HELLO WORLD"}
				assert session.last_call_params == {"chatId": 512}
