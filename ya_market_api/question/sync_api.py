from ya_market_api.base.sync_api_mixin import SyncAPIMixin
from ya_market_api.question.base_api import BaseQuestionAPI
from ya_market_api.question.const import EntityType, EntityOperationType
from ya_market_api.question.dataclass import (
	QuestionListRequest, QuestionListResponse, QuestionAnswerListRequest, QuestionAnswerListResponse,
	QuestionAnswerCreateRequest, QuestionAnswerCreateResponse, QuestionAnswerUpdateRequest,
	QuestionAnswerUpdateResponse, QuestionAnswerDeleteRequest, QuestionAnswerDeleteResponse,
)
from ya_market_api.question.dataclass.entity import EntityId, EntityRequest, EntityCreateResponse

from typing import Optional


class SyncQuestionAPI(SyncAPIMixin, BaseQuestionAPI):
	def get_question_list(self, request: Optional[QuestionListRequest] = None) -> QuestionListResponse:
		request = request or QuestionListRequest()
		response = self.session.post(
			url=self.router.question_list(self.business_id),
			params=request.model_dump_request_params(),
			json=request.model_dump_request_payload(),
		)
		self.validate_response(response)

		return QuestionListResponse.model_validate_json(response.text)

	def get_question_answer_list(self, request: QuestionAnswerListRequest) -> QuestionAnswerListResponse:
		response = self.session.post(
			url=self.router.question_answer_list(self.business_id),
			params=request.model_dump_request_params(),
			json=request.model_dump_request_payload(),
		)
		self.validate_response(response)

		return QuestionAnswerListResponse.model_validate_json(response.text)

	def create_question_answer(self, request: QuestionAnswerCreateRequest) -> QuestionAnswerCreateResponse:
		parent_entity_id = EntityId(id=request.question_id, type=EntityType.QUESTION)
		entity_request = EntityRequest(
			operation_type=EntityOperationType.CREATE,
			parent_entity_id=parent_entity_id,
			text=request.text,
		)
		response = self.session.post(
			url=self.router.question_answer_create(self.business_id),
			json=entity_request.model_dump_request_payload(),
		)
		self.validate_response(response)
		response_payload = EntityCreateResponse.model_validate_json(response.text)

		return QuestionAnswerCreateResponse(answer_id=response_payload.result.entity.id)

	def update_question_answer(self, request: QuestionAnswerUpdateRequest) -> QuestionAnswerUpdateResponse:
		entity_id = EntityId(id=request.answer_id, type=EntityType.ANSWER)
		entity_request = EntityRequest(
			operation_type=EntityOperationType.UPDATE,
			entity_id=entity_id,
			text=request.text,
		)
		response = self.session.post(
			url=self.router.question_answer_update(self.business_id),
			json=entity_request.model_dump_request_payload(),
		)
		self.validate_response(response)

		return QuestionAnswerUpdateResponse()

	def delete_question_answer(self, request: QuestionAnswerDeleteRequest) -> QuestionAnswerDeleteResponse:
		entity_id = EntityId(id=request.answer_id, type=EntityType.ANSWER)
		entity_request = EntityRequest(operation_type=EntityOperationType.DELETE, entity_id=entity_id)
		response = self.session.post(
			url=self.router.question_answer_delete(self.business_id),
			json=entity_request.model_dump_request_payload(),
		)
		self.validate_response(response)

		return QuestionAnswerDeleteResponse()
