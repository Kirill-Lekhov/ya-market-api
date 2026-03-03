from ya_market_api.base.enum_toolkit import allow_unknown

from enum import Enum


class QuestionSortOrderType(Enum):
	CREATED_AT_DESC = "CREATED_AT_DESC"
	CREATED_AT_ASC = "CREATED_AT_ASC"


class EntityOperationType(Enum):
	CREATE = "CREATE"
	UPDATE = "UPDATE"
	DELETE = "DELETE"


class EntityType(Enum):
	QUESTION = "QUESTION"
	ANSWER = "ANSWER"
	COMMENT = "COMMENT"


@allow_unknown
class AuthorType(Enum):
	USER = "USER"
	BUSINESS = "BUSINESS"
	VENDOR = "VENDOR"
	BRAND = "BRAND"


@allow_unknown
class ModerationStatus(Enum):
	PUBLISHED = "PUBLISHED"
	UNMODERATED = "UNMODERATED"
	BANNED = "BANNED"
	DELETED = "DELETED"
