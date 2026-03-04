from enum import Enum


class ChatContextType(Enum):
	ORDER = "ORDER"
	RETURN = "RETURN"
	DIRECT = "DIRECT"


class ChatStatusType(Enum):
	NEW = "NEW"											# новый чат.
	WAITING_FOR_CUSTOMER = "WAITING_FOR_CUSTOMER"		# нужен ответ покупателя.
	WAITING_FOR_PARTNER = "WAITING_FOR_PARTNER"			# нужен ответ магазина.
	WAITING_FOR_ARBITER = "WAITING_FOR_ARBITER"			# нужен ответ арбитра.
	WAITING_FOR_MARKET = "WAITING_FOR_MARKET"			# нужен ответ Маркета.
	FINISHED = "FINISHED"								# чат завершен.


class ChatType(Enum):
	CHAT = "CHAT"				# чат с покупателем.
	ARBITRAGE = "ARBITRAGE"		# спор.


class ChatContextIdentifiableType(Enum):
	ORDER = "ORDER"			# по заказам
	RETURN = "RETURN"		# по возвратам (FBY, FBS и Экспресс).


class ChatMessageSenderType(Enum):
	PARTNER = "PARTNER"			# магазин.
	CUSTOMER = "CUSTOMER"		# покупатель.
	MARKET = "MARKET"			# Маркет (автоматическое сообщение).
	SUPPORT = "SUPPORT"			# сотрудник службы поддержки Маркета.
