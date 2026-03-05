from ya_market_api.base.dataclass.base_request import BaseRequest


class TestSimpleRequest(BaseRequest):
	__test__ = False


class TestRequest(BaseRequest):
	__test__ = False

	QUERY_PARAMS = frozenset({"query_param"})
	PATH_PARAMS = frozenset({"path_param"})
	FILES = frozenset({"file"})

	query_param: str = "QUERY PARAM"
	path_param: str = "PATH PARAM"
	file: bytes = b"FILE"
	payload: str = "PAYLOAD"


class TestBaseRequest:
	def test_model_dump_request_params(self):
		request = TestSimpleRequest()
		assert request.model_dump_request_params() == {}

		request = TestRequest()
		assert request.model_dump_request_params() == {"query_param": "QUERY PARAM"}

	def test_model_dump_request_files(self):
		request = TestSimpleRequest()
		assert request.model_dump_request_files() == {}

		request = TestRequest()
		assert request.model_dump_request_files() == {"file": b"FILE"}

	def test_model_dump_request_payload(self):
		request = TestSimpleRequest()
		assert request.model_dump_request_payload() == {}

		request = TestRequest()
		assert request.model_dump_request_payload() == {"payload": "PAYLOAD"}
