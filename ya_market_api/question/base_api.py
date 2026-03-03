from ya_market_api.base.api import API
from ya_market_api.question.router import QuestionRouter
from ya_market_api.exception import BusinessIdError


class BaseQuestionAPI(API[QuestionRouter]):
	@property
	def business_id(self) -> int:
		if self.config.business_id is None:
			raise BusinessIdError("The business_id was not specified")

		return self.config.business_id

	@staticmethod
	def make_router(base_url: str) -> QuestionRouter:
		return QuestionRouter(base_url)
