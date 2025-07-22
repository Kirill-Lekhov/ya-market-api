from ya_market_api.exception import InvalidResponseError, AuthorizationError, NotFoundError

from http import HTTPStatus

from aiohttp.client import ClientSession, ClientResponse


class AsyncAPIMixin:
	session: ClientSession

	def __init__(self, session: ClientSession, *args, **kwargs) -> None:
		super().__init__(*args, **kwargs)

		self.session = session

	def validate_response(self, response: ClientResponse) -> None:
		if not response.ok:
			if response.status == HTTPStatus.FORBIDDEN or response.status == HTTPStatus.UNAUTHORIZED:
				raise AuthorizationError("Unauthorized")
			elif response.status == HTTPStatus.NOT_FOUND:
				raise NotFoundError("Resource was not found")

			raise InvalidResponseError("Response is not valid")
