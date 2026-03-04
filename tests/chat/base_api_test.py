from ya_market_api.chat.base_api import BaseChatAPI
from ya_market_api.exception import BusinessIdError
from ya_market_api.base.config import Config

import pytest


class TestBaseChatAPI:
	def test_business_id(self):
		config = Config(None, "")
		api = BaseChatAPI(config)

		with pytest.raises(BusinessIdError, match="The business_id was not specified"):
			api.business_id

		config.business_id = 512
		assert api.business_id == 512
