from ya_market_api.exception import InvalidResponseError, AuthorizationError, NotFoundError

from http import HTTPStatus

from requests.sessions import Session
from requests.models import Response


class SyncAPIMixin:
	session: Session

	def __init__(self, session: Session, *args, **kwargs) -> None:
		super().__init__(*args, **kwargs)

		self.session = session

	def validate_response(self, response: Response) -> None:
		if not response.ok:
			if response.status_code == HTTPStatus.FORBIDDEN or response.status_code == HTTPStatus.UNAUTHORIZED:
				raise AuthorizationError("Unauthorized")
			elif response.status_code == HTTPStatus.NOT_FOUND:
				raise NotFoundError("Resource was not found")

			raise InvalidResponseError("Response is not valid")
