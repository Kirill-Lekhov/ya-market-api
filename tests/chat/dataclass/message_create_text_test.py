from ya_market_api.chat.dataclass.message_create_text import Request


class TestRequest:
	def test_model_dump_request_params(self):
		request = Request(chat_id=1, message="hello world")
		assert request.model_dump_request_params() == {"chatId": 1}

	def test_model_dump_request_payload(self):
		request = Request(chat_id=1, message="hello world")
		assert request.model_dump_request_payload() == {"message": "hello world"}
