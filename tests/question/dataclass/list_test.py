from ya_market_api.question.dataclass.list import Request, Question
from ya_market_api.question.const import QuestionSortOrderType

import arrow


class TestRequest:
	def test_serialize_optional_dates(self):
		request = Request()
		assert request.serialize_optional_dates(None) is None
		assert request.serialize_optional_dates(arrow.get(2026, 1, 1, 12, 30, 54)) == "2026-01-01"
		assert request.serialize_optional_dates(arrow.get(2026, 11, 30, 23, 59, 59)) == "2026-11-30"

	def test_model_dump_request_params(self):
		request = Request()
		assert request.model_dump_request_params() == {}

		request = Request(
			limit=10,
			page_token="PAGE_TOKEN",
			category_ids={1, 2, 3},
			date_from=arrow.get(2026, 1, 1),
			date_to=arrow.get(2026, 12, 31),
			need_answer=True,
			sort=QuestionSortOrderType.CREATED_AT_ASC,
		)
		assert request.model_dump_request_params() == {"limit": 10, "pageToken": "PAGE_TOKEN"}

	def test_model_dump_request_payload(self):
		request = Request()
		assert request.model_dump_request_payload() == {}

		request = Request(
			limit=10,
			page_token="PAGE_TOKEN",
			category_ids={1, 2, 3},
			date_from=arrow.get(2026, 1, 1),
			date_to=arrow.get(2026, 12, 31),
			need_answer=True,
			sort=QuestionSortOrderType.CREATED_AT_ASC,
		)
		assert request.model_dump_request_payload() == {
			"categoryIds": [1, 2, 3],
			"dateFrom": "2026-01-01",
			"dateTo": "2026-12-31",
			"needAnswer": True,
			"sort": QuestionSortOrderType.CREATED_AT_ASC.value,
		}


class TestQuestion:
	def test_validate_datetimes(self):
		assert Question.validate_datetimes("2026-01-01T12:30:54+00:00") == arrow.get(2026, 1, 1, 12, 30, 54)
