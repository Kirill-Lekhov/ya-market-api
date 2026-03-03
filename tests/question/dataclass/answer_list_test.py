from ya_market_api.question.dataclass.answer_list import Request, Comment, Answer

import arrow


class TestRequest:
	def test_model_dump_request_params(self):
		request = Request(question_id=1)
		assert request.model_dump_request_params() == {}

		request = Request(question_id=1, limit=10, page_token="PAGE_TOKEN")
		assert request.model_dump_request_params() == {"limit": 10, "pageToken": "PAGE_TOKEN"}

	def test_model_dump_request_payload(self):
		request = Request(question_id=1)
		assert request.model_dump_request_payload() == {"questionId": 1}

		request = Request(question_id=1, limit=10, page_token="PAGE_TOKEN")
		assert request.model_dump_request_payload() == {"questionId": 1}


class TestComment:
	def test_validate_datetimes(self):
		assert Comment.validate_datetimes("2026-01-01T12:30:54+00:00") == arrow.get(2026, 1, 1, 12, 30, 54)


class TestAnswer:
	def test_validate_datetimes(self):
		assert Answer.validate_datetimes("2026-01-01T12:30:54+00:00") == arrow.get(2026, 1, 1, 12, 30, 54)
