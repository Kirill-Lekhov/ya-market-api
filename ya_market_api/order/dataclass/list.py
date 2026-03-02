from ya_market_api.base.const import SellingProgramType, CurrencyType
from ya_market_api.base.dataclass import Region, GPS
from ya_market_api.order.const import (
	OrderSourcePlatformType, OrderStatus, OrderSubstatus, PaymentMethod, PaymentType, OrderBuyerType,
	OrderDeliveryPartnerType, OrderDeliveryType, OrderDeliveryDispatchType, OrderItemInstanceType, OrderItemTag,
	OrderLiftType, OrderVatType, OrderDeliveryEacType,
)

from typing import ClassVar, FrozenSet, Optional, Collection, Set, Dict, Any, List
from datetime import time

from pydantic.main import BaseModel
from pydantic.fields import Field
from pydantic.config import ConfigDict
from pydantic.functional_validators import model_validator, field_validator
from pydantic.functional_serializers import field_serializer
from arrow import Arrow, get as get_arrow


class Dates(BaseModel):
	model_config = ConfigDict(arbitrary_types_allowed=True)

	creation_date_from: Optional[Arrow] = Field(default=None, serialization_alias="creationDateFrom")
	creation_date_to: Optional[Arrow] = Field(default=None, serialization_alias="creationDateTo")
	shipment_date_from: Optional[Arrow] = Field(default=None, serialization_alias="shipmentDateFrom")
	shipment_date_to: Optional[Arrow] = Field(default=None, serialization_alias="shipmentDateTo")
	update_date_from: Optional[Arrow] = Field(default=None, serialization_alias="updateDateFrom")
	update_date_to: Optional[Arrow] = Field(default=None, serialization_alias="updateDateTo")

	@model_validator(mode="after")
	def validate_creation_dates(self):
		if self.creation_date_from and self.creation_date_to:
			if self.creation_date_from > self.creation_date_to:
				raise ValueError("Creation date from cannot be greater than creation date to")

			if (self.creation_date_to - self.creation_date_from).days > 30:
				raise ValueError("Creation date interval must be less than 30 days")

		return self

	@model_validator(mode="after")
	def validate_shipment_dates(self):
		if self.shipment_date_from and self.shipment_date_to:
			if self.shipment_date_from > self.shipment_date_to:
				raise ValueError("Shipment date from cannot be greater than shipment date to")

			if (self.shipment_date_to - self.shipment_date_from).days > 30:
				raise ValueError("Shipment date interval must be less than 30 days")

		return self

	@model_validator(mode="after")
	def validate_update_dates(self):
		if self.update_date_from and self.update_date_to:
			if self.update_date_from > self.update_date_to:
				raise ValueError("Update date from cannot be greater than update date to")

			if (self.update_date_to - self.update_date_from).days > 30:
				raise ValueError("Update date interval must be less than 30 days")

		return self

	@field_serializer("creation_date_from", "creation_date_to", "shipment_date_from", "shipment_date_to", mode="plain")
	def serialize_optional_dates(self, value: Optional[Arrow]) -> Optional[str]:
		if value is None:
			return None

		return value.format("YYYY-MM-DD")

	@field_serializer("update_date_from", "update_date_to", mode="plain")
	def serialize_optional_datetimes(self, value: Optional[Arrow]) -> Optional[str]:
		if value is None:
			return None

		return value.to("UTC").format("YYYY-MM-DD[T]HH:mm:ss[Z]")


class Request(BaseModel):
	QUERY_PARAMS: ClassVar[FrozenSet[str]] = frozenset({"limit", "page_token"})
	model_config = ConfigDict(arbitrary_types_allowed=True)

	# query params
	limit: Optional[int] = Field(default=None, ge=1, le=50)
	page_token: Optional[str] = Field(default=None, serialization_alias="pageToken")

	# payload
	campaign_ids: Optional[Collection[int]] = Field(default=None, ge=1, serialization_alias="campaignIds")
	dates: Optional[Dates] = None
	external_order_ids: Optional[Set[str]] = Field(
		default=None, min_length=1, max_length=50, serialization_alias="externalOrderIds",
	)
	fake: Optional[bool] = None
	order_ids: Optional[Set[int]] = Field(default=None, min_length=1, max_length=50, serialization_alias="orderIds")
	program_types: Optional[Set[SellingProgramType]] = Field(
		default=None, min_length=1, serialization_alias="programTypes",
	)
	source_platforms: Optional[Set[OrderSourcePlatformType]] = Field(
		default=None, min_length=1, serialization_alias="sourcePlatforms",
	)
	statuses: Optional[Set[OrderStatus]] = Field(default=None, min_length=1)
	substatuses: Optional[Set[OrderSubstatus]] = Field(default=None, min_length=1)
	waiting_for_cancellation_approve: Optional[bool] = Field(
		default=None, serialization_alias="waitingForCancellationApprove",
	)

	def model_dump_request_params(self) -> Dict[str, Any]:
		return self.model_dump(include=self.QUERY_PARAMS, by_alias=True, exclude_none=True, mode="json")

	def model_dump_request_payload(self) -> Dict[str, Any]:
		return self.model_dump(exclude=self.QUERY_PARAMS, by_alias=True, exclude_none=True, mode="json")


class Paging(BaseModel):
	next_page_token: Optional[str] = Field(default=None, validation_alias="nextPageToken")


class OrderDeliveryDates(BaseModel):
	model_config = ConfigDict(arbitrary_types_allowed=True)

	from_date: Arrow = Field(validation_alias="fromDate")
	from_time: Optional[time] = Field(default=None, validation_alias="fromTime")
	real_delivery_date: Optional[Arrow] = Field(default=None, validation_alias="realDeliveryDate")
	to_date: Optional[Arrow] = Field(default=None, validation_alias="toDate")
	to_time: Optional[time] = Field(default=None, validation_alias="toTime")

	@field_validator("from_time", "to_time", mode="before")
	@classmethod
	def validate_optional_time(cls, value: Any) -> Optional[time]:
		if value is None:
			return None

		return time.fromisoformat(value)

	@field_validator("real_delivery_date", "to_date", mode="before")
	@classmethod
	def validate_optional_date(cls, value: Any) -> Optional[Arrow]:
		if value is None:
			return None

		return get_arrow(value)

	@field_validator("from_date", mode="before")
	@classmethod
	def validate_date(cls, value: Any) -> Optional[Arrow]:
		return get_arrow(value)


class BriefOrderItemInstance(BaseModel):
	cis: Optional[str] = None
	country_code: Optional[str] = Field(default=None, min_length=2, max_length=2, validation_alias="countryCode")
	gtd: Optional[str] = None
	rnpt: Optional[str] = None
	uin: Optional[str] = None


class OrderBoxLayoutPartialCount(BaseModel):
	current: int = Field(ge=1)
	total: int = Field(ge=2)


class OrderBoxLayoutItem(BaseModel):
	id: int
	full_count: Optional[int] = Field(default=None, validation_alias="fullCount")
	instances: Optional[List[BriefOrderItemInstance]] = None
	partial_count: Optional[OrderBoxLayoutPartialCount] = Field(default=None, validation_alias="partialCount")


class OrderBoxLayout(BaseModel):
	barcode: str
	box_id: int = Field(validation_alias="boxId")
	items: List[OrderBoxLayoutItem] = Field(min_length=1)


class OrderDeliveryAddress(BaseModel):
	apartment: Optional[str] = None
	block: Optional[str] = None
	city: Optional[str] = None
	country: Optional[str] = None
	district: Optional[str] = None
	entrance: Optional[str] = None
	entryphone: Optional[str] = None
	floor: Optional[str] = None
	gps: Optional[GPS] = None
	house: Optional[str] = None
	postcode: Optional[str] = None
	street: Optional[str] = None
	subway: Optional[str] = None


class OrderCourierDelivery(BaseModel):
	address: Optional[OrderDeliveryAddress] = None
	region: Optional[Region] = None


class OrderPickupDelivery(BaseModel):
	model_config = ConfigDict(arbitrary_types_allowed=True)

	address: Optional[OrderDeliveryAddress] = None
	logistic_point_id: Optional[int] = Field(default=None, validation_alias="logisticPointId")
	outlet_code: Optional[str] = Field(default=None, validation_alias="outletCode")
	outlet_storage_limit_date: Optional[Arrow] = Field(default=None, validation_alias="outletStorageLimitDate")
	region: Optional[Region] = None

	@field_validator("outlet_storage_limit_date", mode="before")
	@classmethod
	def validate_optional_date(cls, value: Any) -> Optional[Arrow]:
		if value is None:
			return value

		return get_arrow(value)


class OrderShipment(BaseModel):
	model_config = ConfigDict(arbitrary_types_allowed=True)

	shipment_date: Arrow = Field(validation_alias="shipmentDate")
	id: Optional[int]
	shipment_time: Optional[time] = Field(default=None, validation_alias="shipmentTime")

	@field_validator("shipment_date", mode="before")
	@classmethod
	def validate_date(cls, value: Any) -> Arrow:
		return get_arrow(value)

	@field_validator("shipment_time", mode="before")
	@classmethod
	def validate_optional_time(cls, value: Any) -> Optional[time]:
		if value is None:
			return None

		return time.fromisoformat(value)


class OrderTrack(BaseModel):
	delivery_service_id: int = Field(validation_alias="deliveryServiceId")
	track_code: Optional[str] = Field(default=None, validation_alias="trackCode")


class OrderCourier(BaseModel):
	full_name: Optional[str] = Field(default=None, validation_alias="fullName")
	phone: Optional[str] = None
	phone_extension: Optional[str] = Field(default=None, validation_alias="phoneExtension")
	vehicle_description: Optional[str] = Field(default=None, validation_alias="vehicleDescription")
	vehicle_number: Optional[str] = Field(default=None, validation_alias="vehicleNumber")


class OrderEAC(BaseModel):
	type: OrderDeliveryEacType
	code: Optional[str] = None


class OrderTransfer(BaseModel):
	courier: Optional[OrderCourier] = None
	eac: Optional[OrderEAC] = None


class OrderDelivery(BaseModel):
	dates: OrderDeliveryDates
	delivery_partner_type: OrderDeliveryPartnerType = Field(validation_alias="deliveryPartnerType")
	delivery_service_id: int = Field(validation_alias="deliveryServiceId")
	service_name: str = Field(validation_alias="serviceName")
	type: OrderDeliveryType
	boxes_layout: Optional[List[OrderBoxLayout]] = Field(default=None, validation_alias="boxesLayout")
	courier: Optional[OrderCourierDelivery] = None
	dispatch_type: Optional[OrderDeliveryDispatchType] = Field(default=None, validation_alias="dispatchType")
	estimated: Optional[bool] = None
	pickup: Optional[OrderPickupDelivery] = None
	shipment: Optional[OrderShipment] = None
	tracks: Optional[List[OrderTrack]] = None
	transfer: Optional[OrderTransfer] = None
	warehouse_id: Optional[str] = Field(default=None, validation_alias="warehouseId")


class Currency(BaseModel):
	currency_id: CurrencyType = Field(serialization_alias="currencyId")
	value: float


class DeliveryPrice(BaseModel):
	payment: Optional[Currency] = None
	subsidy: Optional[Currency] = None
	vat: Optional[OrderVatType] = None


class OrderPrice(BaseModel):
	cashback: Optional[Currency] = None
	delivery: Optional[DeliveryPrice] = None
	payment: Optional[Currency] = None
	subsidy: Optional[Currency] = None


class OrderItemInstance(BaseModel):
	cis: Optional[str] = None
	cis_full: Optional[str] = Field(default=None, validation_alias="cisFull")
	country_code: Optional[str] = Field(default=None, min_length=2, max_length=2, validation_alias="countryCode")
	gtd: Optional[str] = None
	rnpt: Optional[str] = None
	uin: Optional[str] = None


class OrderItemPrice(BaseModel):
	cashback: Optional[Currency] = None
	payment: Optional[Currency] = None
	subsidy: Optional[Currency] = None
	vat: Optional[OrderVatType] = None


class OrderItem(BaseModel):
	count: int
	id: int
	offer_id: str = Field(min_length=1, max_length=255, validation_alias="offerId")
	offer_name: str = Field(validation_alias="offerName")
	instances: Optional[List[OrderItemInstance]] = None
	prices: Optional[OrderItemPrice]
	required_instance_types: Optional[List[OrderItemInstanceType]] = Field(
		default=None, validation_alias="requiredInstanceTypes",
	)
	tags: Optional[List[OrderItemTag]] = None


class OrderServices(BaseModel):
	lift_type: Optional[OrderLiftType] = Field(default=None, validation_alias="liftType")


class Order(BaseModel):
	model_config = ConfigDict(arbitrary_types_allowed=True)

	campaign_id: int = Field(ge=1, validation_alias="campaignId")
	created_at: Arrow = Field(validation_alias="creationDate")
	delivery: OrderDelivery
	fake: bool
	items: List[OrderItem]
	order_id: int = Field(validation_alias="orderId")
	payment_method: PaymentMethod = Field(validation_alias="paymentMethod")
	payment_type: PaymentType = Field(validation_alias="paymentType")
	status: OrderStatus
	substatus: OrderSubstatus
	buyer_type: Optional[OrderBuyerType] = Field(default=None, validation_alias="buyerType")
	cancel_requested: Optional[bool] = Field(default=None, validation_alias="cancelRequested")
	external_order_id: Optional[str] = Field(default=None, min_length=1, validation_alias="externalOrderId")
	notes: Optional[str] = None
	prices: Optional[OrderPrice] = None
	program_type: Optional[SellingProgramType] = Field(default=None, validation_alias="programType")
	services: Optional[OrderServices] = None
	source_platform: Optional[OrderSourcePlatformType] = Field(default=None, validation_alias="sourcePlatform")
	updated_at: Optional[Arrow] = Field(default=None, validation_alias="updateDate")

	@field_validator("created_at", mode="before")
	@classmethod
	def validate_datetimes(cls, value: Any) -> Arrow:
		return get_arrow(value)

	@field_validator("updated_at", mode="before")
	@classmethod
	def validate_optional_datetimes(cls, value: Any) -> Optional[Arrow]:
		if value is None:
			return None

		return get_arrow(value)


class Response(BaseModel):
	orders: List[Order] = Field(max_length=50)
	paging: Optional[Paging] = None
