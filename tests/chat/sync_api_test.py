from ya_market_api.base.sync_config import SyncConfig
from ya_market_api.chat.sync_api import SyncChatAPI
from ya_market_api.chat.dataclass import (
	ChatListRequest, ChatGetRequest, ChatMessageListRequest, ChatMessageGetRequest, ChatMessageCreateTextRequest,
	ChatMessageCreateFileRequest,
)
from ya_market_api.chat.const import ChatType

from unittest.mock import patch, Mock


class TestChatSyncAPI:
	def test_get_chat_list(self):
		session = Mock()
		session.post.return_value.text = "RAW DATA"
		config = SyncConfig(session, "", business_id=1)
		api = SyncChatAPI(config)
		request = ChatListRequest(limit=20, page_token="PAGE TOKEN", types={ChatType.CHAT})

		with patch("ya_market_api.chat.sync_api.ChatListResponse") as ChatListResponseMock:
			ChatListResponseMock.model_validate_json.return_value = "DESERIALIZED DATA"

			with patch.object(api, "validate_response") as validate_response_mock:
				assert api.get_chat_list() == "DESERIALIZED DATA"
				ChatListResponseMock.model_validate_json.assert_called_once_with("RAW DATA")
				validate_response_mock.assert_called_once_with(session.post.return_value)
				session.post.assert_called_once_with(url=api.router.chat_list(1), params={}, json={})

				session.post.reset_mock()
				assert api.get_chat_list(request) == "DESERIALIZED DATA"
				session.post.assert_called_once_with(
					url=api.router.chat_list(1),
					params={"limit": 20, "pageToken": "PAGE TOKEN"},
					json={"types": [ChatType.CHAT.value]},
				)

	def test_get_chat(self):
		session = Mock()
		session.get.return_value.text = "RAW DATA"
		config = SyncConfig(session, "", business_id=1)
		api = SyncChatAPI(config)
		request = ChatGetRequest(chat_id=512)

		with patch("ya_market_api.chat.sync_api.ChatGetResponse") as ChatGetResponseMock:
			ChatGetResponseMock.model_validate_json.return_value = "DESERIALIZED DATA"

			with patch.object(api, "validate_response") as validate_response_mock:
				assert api.get_chat(request) == "DESERIALIZED DATA"
				ChatGetResponseMock.model_validate_json.assert_called_once_with("RAW DATA")
				validate_response_mock.assert_called_once_with(session.get.return_value)
				session.get.assert_called_once_with(url=api.router.chat_get(1), params={"chatId": 512})

	def test_get_chat_message_list(self):
		session = Mock()
		session.post.return_value.text = "RAW DATA"
		config = SyncConfig(session, "", business_id=1)
		api = SyncChatAPI(config)
		request = ChatMessageListRequest(chat_id=512)

		with patch("ya_market_api.chat.sync_api.ChatMessageListResponse") as ChatMessageListResponseMock:
			ChatMessageListResponseMock.model_validate_json.return_value = "DESERIALIZED DATA"

			with patch.object(api, "validate_response") as validate_response_mock:
				assert api.get_chat_message_list(request) == "DESERIALIZED DATA"
				ChatMessageListResponseMock.model_validate_json.assert_called_once_with("RAW DATA")
				validate_response_mock.assert_called_once_with(session.post.return_value)
				session.post.assert_called_once_with(
					url=api.router.chat_message_list(1),
					params={
						"chatId": 512,
					},
					json={},
				)

				session.post.reset_mock()
				request = ChatMessageListRequest(chat_id=512, limit=20, page_token="PAGE TOKEN", message_id_from=1024)
				assert api.get_chat_message_list(request) == "DESERIALIZED DATA"
				session.post.assert_called_once_with(
					url=api.router.chat_message_list(1),
					params={
						"chatId": 512,
						"limit": 20,
						"pageToken": "PAGE TOKEN",
					},
					json={
						"messageIdFrom": 1024,
					},
				)

	def test_get_chat_message(self):
		session = Mock()
		session.get.return_value.text = "RAW DATA"
		config = SyncConfig(session, "", business_id=1)
		api = SyncChatAPI(config)
		request = ChatMessageGetRequest(chat_id=512, message_id=1024)

		with patch("ya_market_api.chat.sync_api.ChatMessageGetResponse") as ChatMessageGetResponseMock:
			ChatMessageGetResponseMock.model_validate_json.return_value = "DESERIALIZED DATA"

			with patch.object(api, "validate_response") as validate_response_mock:
				assert api.get_chat_message(request) == "DESERIALIZED DATA"
				ChatMessageGetResponseMock.model_validate_json.assert_called_once_with("RAW DATA")
				validate_response_mock.assert_called_once_with(session.get.return_value)
				session.get.assert_called_once_with(
					url=api.router.chat_message_get(1),
					params={"chatId": 512, "messageId": 1024},
				)

	def test_create_chat_message_text(self):
		session = Mock()
		session.post.return_value.text = "RAW DATA"
		config = SyncConfig(session, "", business_id=1)
		api = SyncChatAPI(config)
		request = ChatMessageCreateTextRequest(chat_id=512, message="HELLO WORLD")

		with patch("ya_market_api.chat.sync_api.ChatMessageCreateTextResponse") as ChatMessageCreateTextResponseMock:
			ChatMessageCreateTextResponseMock.model_validate_json.return_value = "DESERIALIZED DATA"

			with patch.object(api, "validate_response") as validate_response_mock:
				assert api.create_chat_message_text(request) == "DESERIALIZED DATA"
				ChatMessageCreateTextResponseMock.model_validate_json.assert_called_once_with("RAW DATA")
				validate_response_mock.assert_called_once_with(session.post.return_value)
				session.post.assert_called_once_with(
					url=api.router.chat_message_create_text(1),
					params={
						"chatId": 512,
					},
					json={
						"message": "HELLO WORLD",
					},
				)

	def test_create_chat_message_file(self):
		session = Mock()
		session.post.return_value.text = "RAW DATA"
		config = SyncConfig(session, "", business_id=1)
		api = SyncChatAPI(config)
		request = ChatMessageCreateFileRequest(chat_id=512, file=b"HELLO WORLD")

		with patch("ya_market_api.chat.sync_api.ChatMessageCreateFileResponse") as ChatMessageCreateFileResponseMock:
			ChatMessageCreateFileResponseMock.model_validate_json.return_value = "DESERIALIZED DATA"

			with patch.object(api, "validate_response") as validate_response_mock:
				assert api.create_chat_message_file(request) == "DESERIALIZED DATA"
				ChatMessageCreateFileResponseMock.model_validate_json.assert_called_once_with("RAW DATA")
				validate_response_mock.assert_called_once_with(session.post.return_value)
				session.post.assert_called_once_with(
					url=api.router.chat_message_create_file(1),
					params={
						"chatId": 512,
					},
					files={
						"file": b"HELLO WORLD",
					},
				)
