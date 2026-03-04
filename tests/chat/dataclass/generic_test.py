from ya_market_api.chat.dataclass.generic import Chat, ChatMessage

import arrow


class TestChat:
	def test_validate_datetimes(self):
		assert Chat.validate_datetimes("2026-06-01T12:30:54+00:00") == arrow.get(2026, 6, 1, 12, 30, 54)


class TestChatMessage:
	def test_validate_datetimes(self):
		assert ChatMessage.validate_datetimes("2026-06-01T12:30:54+00:00") == arrow.get(2026, 6, 1, 12, 30, 54)
