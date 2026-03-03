from ya_market_api.question.router import QuestionRouter


class TestQuestionRouter:
	def test_question_list(self):
		router = QuestionRouter("")
		assert router.question_list(1) == "/v1/businesses/1/goods-questions"

	def test_question_answer_list(self):
		router = QuestionRouter("")
		assert router.question_answer_list(1) == "/v1/businesses/1/goods-questions/answers"

	def test_question_answer_create(self):
		router = QuestionRouter("")
		assert router.question_answer_create(1) == "/v1/businesses/1/goods-questions/update"

	def test_question_answer_update(self):
		router = QuestionRouter("")
		assert router.question_answer_update(1) == "/v1/businesses/1/goods-questions/update"

	def test_question_answer_delete(self):
		router = QuestionRouter("")
		assert router.question_answer_delete(1) == "/v1/businesses/1/goods-questions/update"
