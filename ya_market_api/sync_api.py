from ya_market_api.const import Header
from ya_market_api.generic.requests.auth import APIKeyAuth
from ya_market_api.guide.sync_api import SyncGuideAPI

from requests.sessions import Session


class SyncAPI:
	guide: SyncGuideAPI
	session: Session

	def __init__(self, session: Session) -> None:
		self.session = session
		self.guide = SyncGuideAPI(session)

	@classmethod
	def build(cls, api_key: str) -> "SyncAPI":
		session = cls.make_session(api_key)

		return cls(session)

	@staticmethod
	def make_session(api_key: str) -> Session:
		session = Session()
		session.auth = APIKeyAuth(api_key, Header.API_KEY.value)

		return session
