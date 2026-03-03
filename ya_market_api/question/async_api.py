from ya_market_api.base.async_api_mixin import AsyncAPIMixin
from ya_market_api.question.base_api import BaseQuestionAPI
from ya_market_api.question.const import EntityType, EntityOperationType
from ya_market_api.question.dataclass import (
	QuestionListRequest, QuestionListResponse, QuestionAnswerListRequest, QuestionAnswerListResponse,
	QuestionAnswerCreateRequest, QuestionAnswerCreateResponse, QuestionAnswerUpdateRequest,
	QuestionAnswerUpdateResponse, QuestionAnswerDeleteRequest, QuestionAnswerDeleteResponse,
)
from ya_market_api.question.dataclass.entity import EntityId, EntityRequest, EntityCreateResponse

from typing import Optional


class AsyncQuestionAPI(AsyncAPIMixin, BaseQuestionAPI):
	async def get_question_list(self, request: Optional[QuestionListRequest] = None) -> QuestionListResponse:
		request = request or QuestionListRequest()
		url = self.router.question_list(self.business_id)

		async with self.session.post(
			url=url,
			params=request.model_dump_request_params(),
			json=request.model_dump_request_payload(),
		) as response:
			self.validate_response(response)
			return QuestionListResponse.model_validate_json(await response.text())

	async def get_question_answer_list(self, request: QuestionAnswerListRequest) -> QuestionAnswerListResponse:
		url = self.router.question_answer_list(self.business_id)

		async with self.session.post(
			url=url,
			params=request.model_dump_request_params(),
			json=request.model_dump_request_payload(),
		) as response:
			self.validate_response(response)
			return QuestionAnswerListResponse.model_validate_json(await response.text())

	async def create_question_answer(self, request: QuestionAnswerCreateRequest) -> QuestionAnswerCreateResponse:
		url = self.router.question_answer_create(self.business_id)
		parent_entity_id = EntityId(id=request.question_id, type=EntityType.QUESTION)
		entity_request = EntityRequest(
			operation_type=EntityOperationType.CREATE,
			parent_entity_id=parent_entity_id,
			text=request.text,
		)

		async with self.session.post(url=url, json=entity_request.model_dump_request_payload()) as response:
			self.validate_response(response)
			response_payload = EntityCreateResponse.model_validate_json(await response.text())

			return QuestionAnswerCreateResponse(answer_id=response_payload.result.entity.id)

	async def update_question_answer(self, request: QuestionAnswerUpdateRequest) -> QuestionAnswerUpdateResponse:
		url = self.router.question_answer_update(self.business_id)
		entity_id = EntityId(id=request.answer_id, type=EntityType.ANSWER)
		entity_request = EntityRequest(
			operation_type=EntityOperationType.UPDATE,
			entity_id=entity_id,
			text=request.text,
		)

		async with self.session.post(url=url, json=entity_request.model_dump_request_payload()) as response:
			self.validate_response(response)

			return QuestionAnswerUpdateResponse()

	async def delete_question_answer(self, request: QuestionAnswerDeleteRequest) -> QuestionAnswerDeleteResponse:
		url = self.router.question_answer_delete(self.business_id)
		entity_id = EntityId(id=request.answer_id, type=EntityType.ANSWER)
		entity_request = EntityRequest(operation_type=EntityOperationType.DELETE, entity_id=entity_id)

		async with self.session.post(url=url, json=entity_request.model_dump_request_payload()) as response:
			self.validate_response(response)

			return QuestionAnswerDeleteResponse()
