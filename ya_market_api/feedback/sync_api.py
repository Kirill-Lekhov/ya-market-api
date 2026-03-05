from ya_market_api.base.sync_api_mixin import SyncAPIMixin
from ya_market_api.feedback.base_api import BaseFeedbackAPI
from ya_market_api.feedback.dataclass import (
	FeedbackListRequest, FeedbackListResponse, FeedbackCommentListRequest, FeedbackCommentListResponse,
	FeedbackCommentCreateRequest, FeedbackCommentCreateResponse, FeedbackCommentUpdateRequest, FeedbackCommentUpdateResponse,
	FeedbackCommentDeleteRequest, FeedbackCommentDeleteResponse, FeedbackReactionSkipRequest,
	FeedbackReactionSkipResponse,
)

from typing import Optional


class SyncFeedbackAPI(SyncAPIMixin, BaseFeedbackAPI):
	def get_feedback_list(self, request: Optional[FeedbackListRequest] = None) -> FeedbackListResponse:
		request = request or FeedbackListRequest()
		response = self.session.post(
			url=self.router.feedback_list(self.business_id),
			params=request.model_dump_request_params(),
			json=request.model_dump_request_payload(),
		)
		self.validate_response(response)

		return FeedbackListResponse.model_validate_json(response.text)

	def get_feedback_comment_list(self, request: FeedbackCommentListRequest) -> FeedbackCommentListResponse:
		response = self.session.post(
			url=self.router.feedback_comment_list(self.business_id),
			params=request.model_dump_request_params(),
			json=request.model_dump_request_payload(),
		)
		self.validate_response(response)

		return FeedbackCommentListResponse.model_validate_json(response.text)

	def create_feedback_comment(self, request: FeedbackCommentCreateRequest) -> FeedbackCommentCreateResponse:
		response = self.session.post(
			url=self.router.feedback_comment_add(self.business_id),
			json=request.model_dump_request_payload(),
		)
		self.validate_response(response)

		return FeedbackCommentCreateResponse.model_validate_json(response.text)

	def update_feedback_comment(self, request: FeedbackCommentUpdateRequest) -> FeedbackCommentUpdateResponse:
		response = self.session.post(
			url=self.router.feedback_comment_update(self.business_id),
			json=request.model_dump_request_payload(),
		)
		self.validate_response(response)

		return FeedbackCommentUpdateResponse.model_validate_json(response.text)

	def delete_feedback_comment(self, request: FeedbackCommentDeleteRequest) -> FeedbackCommentDeleteResponse:
		response = self.session.post(
			url=self.router.feedback_comment_delete(self.business_id),
			json=request.model_dump_request_payload(),
		)
		self.validate_response(response)

		return FeedbackCommentDeleteResponse.model_validate_json(response.text)

	def skip_feedback_reaction(self, request: FeedbackReactionSkipRequest) -> FeedbackReactionSkipResponse:
		response = self.session.post(
			url=self.router.feedback_reaction_skip(self.business_id),
			json=request.model_dump_request_payload(),
		)
		self.validate_response(response)

		return FeedbackReactionSkipResponse.model_validate_json(response.text)
