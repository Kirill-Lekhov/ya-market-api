from ya_market_api.question.sync_api import SyncQuestionAPI
from ya_market_api.question.dataclass import (
	QuestionListRequest, QuestionAnswerListRequest, QuestionAnswerCreateRequest, QuestionAnswerCreateResponse,
	QuestionAnswerUpdateRequest, QuestionAnswerUpdateResponse, QuestionAnswerDeleteRequest,
	QuestionAnswerDeleteResponse,
)
from ya_market_api.question.const import EntityOperationType, EntityType
from ya_market_api.base.sync_config import SyncConfig

from unittest.mock import patch, Mock


class TestSyncQuestionAPI:
	def test_get_question_list(self):
		session = Mock()
		session.post.return_value.text = "RAW DATA"
		config = SyncConfig(session, "", business_id=1)
		api = SyncQuestionAPI(config)
		request = QuestionListRequest(limit=50, page_token="PAGE TOKEN", need_answer=True)

		with patch("ya_market_api.question.sync_api.QuestionListResponse") as QuestionListResponseMock:
			QuestionListResponseMock.model_validate_json.return_value = "DESERIALIZED DATA"

			with patch.object(api, "validate_response") as validate_response_mock:
				assert api.get_question_list() == "DESERIALIZED DATA"
				QuestionListResponseMock.model_validate_json.assert_called_once_with("RAW DATA")
				validate_response_mock.assert_called_once_with(session.post.return_value)
				session.post.assert_called_once_with(url=api.router.question_list(1), params={}, json={})

				session.post.reset_mock()
				assert api.get_question_list(request) == "DESERIALIZED DATA"
				session.post.assert_called_once_with(
					url=api.router.question_list(1),
					params={"limit": 50, "pageToken": "PAGE TOKEN"},
					json={"needAnswer": True},
				)

	def test_get_question_answer_list(self):
		session = Mock()
		session.post.return_value.text = "RAW DATA"
		config = SyncConfig(session, "", business_id=1)
		api = SyncQuestionAPI(config)
		request = QuestionAnswerListRequest(limit=50, page_token="PAGE TOKEN", question_id=512)

		with patch("ya_market_api.question.sync_api.QuestionAnswerListResponse") as QuestionAnswerListResponseMock:
			QuestionAnswerListResponseMock.model_validate_json.return_value = "DESERIALIZED DATA"

			with patch.object(api, "validate_response") as validate_response_mock:
				assert api.get_question_answer_list(request) == "DESERIALIZED DATA"
				QuestionAnswerListResponseMock.model_validate_json.assert_called_once_with("RAW DATA")
				validate_response_mock.assert_called_once_with(session.post.return_value)
				session.post.assert_called_once_with(
					url=api.router.question_answer_list(1),
					params={"limit": 50, "pageToken": "PAGE TOKEN"},
					json={"questionId": 512},
				)

	def test_create_question_answer(self):
		session = Mock()
		session.post.return_value.text = "RAW DATA"
		config = SyncConfig(session, "", business_id=1)
		api = SyncQuestionAPI(config)
		request = QuestionAnswerCreateRequest(question_id=512, text="HELLO WORLD")

		with patch("ya_market_api.question.sync_api.EntityCreateResponse") as EntityCreateResponseMock:
			EntityCreateResponseMock.model_validate_json.return_value.result.entity.id = 1024

			with patch.object(api, "validate_response") as validate_response_mock:
				assert api.create_question_answer(request) == QuestionAnswerCreateResponse(answer_id=1024)
				EntityCreateResponseMock.model_validate_json.assert_called_once_with("RAW DATA")
				validate_response_mock.assert_called_once_with(session.post.return_value)
				session.post.assert_called_once_with(
					url=api.router.question_answer_create(1),
					json={
						"operationType": EntityOperationType.CREATE.value,
						"parentEntityId": {
							"id": 512,
							"type": EntityType.QUESTION.value,
						},
						"text": "HELLO WORLD",
					},
				)

	def test_update_question_answer(self):
		session = Mock()
		session.post.return_value.text = "RAW DATA"
		config = SyncConfig(session, "", business_id=1)
		api = SyncQuestionAPI(config)
		request = QuestionAnswerUpdateRequest(answer_id=512, text="HELLO WORLD")

		with patch.object(api, "validate_response") as validate_response_mock:
			assert api.update_question_answer(request) == QuestionAnswerUpdateResponse()
			validate_response_mock.assert_called_once_with(session.post.return_value)
			session.post.assert_called_once_with(
				url=api.router.question_answer_update(1),
				json={
					"operationType": EntityOperationType.UPDATE.value,
					"entityId": {
						"id": 512,
						"type": EntityType.ANSWER.value,
					},
					"text": "HELLO WORLD",
				},
			)

	def test_delete_question_answer(self):
		session = Mock()
		session.post.return_value.text = "RAW DATA"
		config = SyncConfig(session, "", business_id=1)
		api = SyncQuestionAPI(config)
		request = QuestionAnswerDeleteRequest(answer_id=512)

		with patch.object(api, "validate_response") as validate_response_mock:
			assert api.delete_question_answer(request) == QuestionAnswerDeleteResponse()
			validate_response_mock.assert_called_once_with(session.post.return_value)
			session.post.assert_called_once_with(
				url=api.router.question_answer_delete(1),
				json={
					"operationType": EntityOperationType.DELETE.value,
					"entityId": {
						"id": 512,
						"type": EntityType.ANSWER.value,
					},
				},
			)
