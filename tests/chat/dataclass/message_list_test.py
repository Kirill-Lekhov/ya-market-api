from ya_market_api.chat.dataclass.message_list import Request


class TestRequest:
	def test_model_dump_request_params(self):
		request = Request(chat_id=1)
		assert request.model_dump_request_params() == {"chatId": 1}

		request = Request(chat_id=1, limit=100, page_token="PAGE TOKEN")
		assert request.model_dump_request_params() == {"chatId": 1, "limit": 100, "pageToken": "PAGE TOKEN"}

	def test_model_dump_request_payload(self):
		request = Request(chat_id=1)
		assert request.model_dump_request_payload() == {}

		request = Request(chat_id=1, message_id_from=112)
		assert request.model_dump_request_payload() == {"messageIdFrom": 112}
