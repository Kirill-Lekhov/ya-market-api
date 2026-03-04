from ya_market_api.chat.dataclass.list import ChatContext, Request
from ya_market_api.chat.const import ChatContextType, ChatContextIdentifiableType, ChatStatusType, ChatType


class TestRequest:
	def test_model_dump_request_params(self):
		request = Request()
		assert request.model_dump_request_params() == {}

		request = Request(limit=20, page_token="PAGE TOKEN")
		assert request.model_dump_request_params() == {"limit": 20, "pageToken": "PAGE TOKEN"}

	def test_model_dump_request_payload(self):
		request = Request()
		assert request.model_dump_request_payload() == {}

		request = Request(
			contexts={
				ChatContext(
					id=1,
					type=ChatContextIdentifiableType.ORDER,
				),
			},
			context_types={
				ChatContextType.RETURN,
			},
			statuses={
				ChatStatusType.FINISHED,
			},
			types={
				ChatType.ARBITRAGE,
			},
		)
		assert request.model_dump_request_payload() == {
			"contexts": [{
				"id": 1,
				"type": ChatContextIdentifiableType.ORDER.value,
			}],
			"contextTypes": [
				ChatContextType.RETURN.value,
			],
			"statuses": [
				ChatStatusType.FINISHED.value,
			],
			"types": [
				ChatType.ARBITRAGE.value,
			],
		}
