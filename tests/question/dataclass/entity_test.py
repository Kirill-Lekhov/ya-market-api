from ya_market_api.question.dataclass.entity import EntityRequest, EntityId
from ya_market_api.question.const import EntityOperationType, EntityType


class TestEntityRequest:
	def test_model_dump_request_payload(self):
		request = EntityRequest.model_validate({"operation_type": EntityOperationType.CREATE})
		assert request.model_dump_request_payload() == {"operationType": EntityOperationType.CREATE.value}

		parent_id = EntityId(id=1, type=EntityType.QUESTION)
		entity_id = EntityId(id=1, type=EntityType.ANSWER)
		request = EntityRequest.model_validate({
			"operation_type": EntityOperationType.UPDATE,
			"entity_id": entity_id,
			"parent_entity_id": parent_id,
			"text": "TEXT",
		})
		assert request.model_dump_request_payload() == {
			"operationType": EntityOperationType.UPDATE.value,
			"entityId": {
				"id": 1,
				"type": EntityType.ANSWER.value,
			},
			"parentEntityId": {
				"id": 1,
				"type": EntityType.QUESTION.value,
			},
			"text": "TEXT",
		}
