from tests.fake_async_session import FakeAsyncSession
from ya_market_api.question.async_api import AsyncQuestionAPI
from ya_market_api.question.dataclass import (
	QuestionListRequest, QuestionAnswerListRequest, QuestionAnswerCreateRequest, QuestionAnswerCreateResponse,
	QuestionAnswerUpdateRequest, QuestionAnswerUpdateResponse, QuestionAnswerDeleteRequest,
	QuestionAnswerDeleteResponse,
)
from ya_market_api.question.const import EntityOperationType, EntityType
from ya_market_api.base.async_config import AsyncConfig

from unittest.mock import patch

import pytest


class TestAsyncQuestionAPI:
	@pytest.mark.asyncio()
	async def test_get_question_list(self):
		session = FakeAsyncSession("RAW DATA")
		config = AsyncConfig(session, "", business_id=1)		# type: ignore - for testing purposes
		api = AsyncQuestionAPI(config)
		request = QuestionListRequest(limit=50, page_token="PAGE TOKEN", need_answer=True)

		with patch("ya_market_api.question.async_api.QuestionListResponse") as QuestionListResponseMock:
			QuestionListResponseMock.model_validate_json.return_value = "DESERIALIZED DATA"

			with patch.object(api, "validate_response") as validate_response_mock:
				assert await api.get_question_list() == "DESERIALIZED DATA"
				QuestionListResponseMock.model_validate_json.assert_called_once_with("RAW DATA")
				validate_response_mock.assert_called_once_with(session.response)
				assert session.last_call_method == "POST"
				assert session.last_call_url == api.router.question_list(1)
				assert session.last_call_json == {}
				assert session.last_call_params == {}

				assert await api.get_question_list(request) == "DESERIALIZED DATA"
				assert session.last_call_method == "POST"
				assert session.last_call_url == api.router.question_list(1)
				assert session.last_call_json == {"needAnswer": True}
				assert session.last_call_params == {"limit": 50, "pageToken": "PAGE TOKEN"}

	@pytest.mark.asyncio()
	async def test_get_question_answer_list(self):
		session = FakeAsyncSession("RAW DATA")
		config = AsyncConfig(session, "", business_id=1)		# type: ignore - for testing purposes
		api = AsyncQuestionAPI(config)
		request = QuestionAnswerListRequest(limit=50, page_token="PAGE TOKEN", question_id=512)

		with patch("ya_market_api.question.async_api.QuestionAnswerListResponse") as QuestionAnswerListResponseMock:
			QuestionAnswerListResponseMock.model_validate_json.return_value = "DESERIALIZED DATA"

			with patch.object(api, "validate_response") as validate_response_mock:
				assert await api.get_question_answer_list(request) == "DESERIALIZED DATA"
				QuestionAnswerListResponseMock.model_validate_json.assert_called_once_with("RAW DATA")
				validate_response_mock.assert_called_once_with(session.response)
				assert session.last_call_method == "POST"
				assert session.last_call_url == api.router.question_answer_list(1)
				assert session.last_call_json == {"questionId": 512}
				assert session.last_call_params == {"limit": 50, "pageToken": "PAGE TOKEN"}

	@pytest.mark.asyncio()
	async def test_create_question_answer(self):
		session = FakeAsyncSession("RAW DATA")
		config = AsyncConfig(session, "", business_id=1)		# type: ignore - for testing purposes
		api = AsyncQuestionAPI(config)
		request = QuestionAnswerCreateRequest(question_id=512, text="HELLO WORLD")

		with patch("ya_market_api.question.async_api.EntityCreateResponse") as EntityCreateResponseMock:
			EntityCreateResponseMock.model_validate_json.return_value.result.entity.id = 256

			with patch.object(api, "validate_response") as validate_response_mock:
				assert await api.create_question_answer(request) == QuestionAnswerCreateResponse(answer_id=256)
				EntityCreateResponseMock.model_validate_json.assert_called_once_with("RAW DATA")
				validate_response_mock.assert_called_once_with(session.response)
				assert session.last_call_method == "POST"
				assert session.last_call_url == api.router.question_answer_create(1)
				assert session.last_call_json == {
					"operationType": EntityOperationType.CREATE.value,
					"parentEntityId": {
						"id": 512,
						"type": EntityType.QUESTION.value,
					},
					"text": "HELLO WORLD",
				}
				assert session.last_call_params is None

	@pytest.mark.asyncio()
	async def test_update_question_answer(self):
		session = FakeAsyncSession("RAW DATA")
		config = AsyncConfig(session, "", business_id=1)		# type: ignore - for testing purposes
		api = AsyncQuestionAPI(config)
		request = QuestionAnswerUpdateRequest(answer_id=512, text="HELLO WORLD")

		with patch.object(api, "validate_response") as validate_response_mock:
			assert await api.update_question_answer(request) == QuestionAnswerUpdateResponse()
			validate_response_mock.assert_called_once_with(session.response)
			assert session.last_call_method == "POST"
			assert session.last_call_url == api.router.question_answer_update(1)
			assert session.last_call_json == {
				"operationType": EntityOperationType.UPDATE.value,
				"entityId": {
					"id": 512,
					"type": EntityType.ANSWER.value,
				},
				"text": "HELLO WORLD",
			}
			assert session.last_call_params is None

	@pytest.mark.asyncio()
	async def test_delete_question_answer(self):
		session = FakeAsyncSession("RAW DATA")
		config = AsyncConfig(session, "", business_id=1)		# type: ignore - for testing purposes
		api = AsyncQuestionAPI(config)
		request = QuestionAnswerDeleteRequest(answer_id=512)

		with patch.object(api, "validate_response") as validate_response_mock:
			assert await api.delete_question_answer(request) == QuestionAnswerDeleteResponse()
			validate_response_mock.assert_called_once_with(session.response)
			assert session.last_call_method == "POST"
			assert session.last_call_url == api.router.question_answer_delete(1)
			assert session.last_call_json == {
				"operationType": EntityOperationType.DELETE.value,
				"entityId": {
					"id": 512,
					"type": EntityType.ANSWER.value,
				},
			}
			assert session.last_call_params is None
