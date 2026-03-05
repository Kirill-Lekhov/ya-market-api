from ya_market_api.question.dataclass.answer_list import Comment, Answer

import arrow


class TestComment:
	def test_validate_datetimes(self):
		assert Comment.validate_datetimes("2026-01-01T12:30:54+00:00") == arrow.get(2026, 1, 1, 12, 30, 54)


class TestAnswer:
	def test_validate_datetimes(self):
		assert Answer.validate_datetimes("2026-01-01T12:30:54+00:00") == arrow.get(2026, 1, 1, 12, 30, 54)
