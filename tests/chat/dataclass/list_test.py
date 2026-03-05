from ya_market_api.chat.dataclass.list import ChatContext
from ya_market_api.chat.const import ChatContextIdentifiableType


class TestChatContext:
	def test___hash__(self):
		context = ChatContext(id=1, type=ChatContextIdentifiableType.RETURN)
		assert hash(context) == hash((1, ChatContextIdentifiableType.RETURN))
