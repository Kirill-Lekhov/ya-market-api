from ya_market_api.base.router import Router


class ChatRouter(Router):
	def chat_get(self, business_id: int) -> str:
		return f"{self.base_url}/v2/businesses/{business_id}/chat"

	def chat_list(self, business_id: int) -> str:
		return f"{self.base_url}/v2/businesses/{business_id}/chats"

	def chat_message_list(self, business_id: int) -> str:
		return f"{self.base_url}/v2/businesses/{business_id}/chats/history"

	def chat_message_get(self, business_id: int) -> str:
		return f"{self.base_url}/v2/businesses/{business_id}/chats/message"

	def chat_message_create_text(self, business_id: int) -> str:
		return f"{self.base_url}/v2/businesses/{business_id}/chats/message"

	def chat_message_create_file(self, business_id: int) -> str:
		return f"{self.base_url}/v2/businesses/{business_id}/chats/file/send"
