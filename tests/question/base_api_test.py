from ya_market_api.question.base_api import BaseQuestionAPI
from ya_market_api.exception import BusinessIdError
from ya_market_api.base.config import Config

import pytest


class TestBaseQuestionAPI:
	def test_business_id(self):
		config = Config(None, "")
		api = BaseQuestionAPI(config)

		with pytest.raises(BusinessIdError, match="The business_id was not specified"):
			api.business_id

		config.business_id = 512
		assert api.business_id == 512
