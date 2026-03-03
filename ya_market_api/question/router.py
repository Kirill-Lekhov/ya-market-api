from ya_market_api.base.router import Router


class QuestionRouter(Router):
	def question_list(self, business_id: int) -> str:
		return f"{self.base_url}/v1/businesses/{business_id}/goods-questions"

	def question_answer_list(self, business_id: int) -> str:
		return f"{self.base_url}/v1/businesses/{business_id}/goods-questions/answers"

	def question_answer_create(self, business_id: int) -> str:
		return f"{self.base_url}/v1/businesses/{business_id}/goods-questions/update"

	def question_answer_update(self, business_id: int) -> str:
		return f"{self.base_url}/v1/businesses/{business_id}/goods-questions/update"

	def question_answer_delete(self, business_id: int) -> str:
		return f"{self.base_url}/v1/businesses/{business_id}/goods-questions/update"
