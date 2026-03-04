from ya_market_api.chat.router import ChatRouter


class TestChatRouter:
	def test_chat_get(self):
		router = ChatRouter("")
		assert router.chat_get(0) == "/v2/businesses/0/chat"

	def test_chat_list(self):
		router = ChatRouter("")
		assert router.chat_list(0) == "/v2/businesses/0/chats"

	def test_chat_message_list(self):
		router = ChatRouter("")
		assert router.chat_message_list(0) == "/v2/businesses/0/chats/history"

	def test_chat_message_get(self):
		router = ChatRouter("")
		assert router.chat_message_get(0) == "/v2/businesses/0/chats/message"

	def test_chat_message_create_text(self):
		router = ChatRouter("")
		assert router.chat_message_create_text(0) == "/v2/businesses/0/chats/message"

	def test_chat_message_create_file(self):
		router = ChatRouter("")
		assert router.chat_message_create_file(0) == "/v2/businesses/0/chats/file/send"
