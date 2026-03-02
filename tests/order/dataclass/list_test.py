from ya_market_api.order.dataclass.list import Dates, OrderDeliveryDates, OrderPickupDelivery, OrderShipment, Order

import datetime

import arrow
import pytest
from pydantic_core import ValidationError


class TestDates:
	def test_validate_creation_dates(self):
		Dates(creation_date_from=arrow.get())
		Dates(creation_date_to=arrow.get())
		Dates(creation_date_from=arrow.get(), creation_date_to=arrow.get())

		with pytest.raises(ValidationError, match="Creation date from cannot be greater than creation date to"):
			Dates(creation_date_from=arrow.get("2026-01-10"), creation_date_to=arrow.get("2026-01-01"))

		with pytest.raises(ValidationError, match="Creation date interval must be less than 30 days"):
			Dates(creation_date_from=arrow.get("2026-01-01"), creation_date_to=arrow.get("2026-06-01"))

	def test_validate_shipment_dates(self):
		Dates(shipment_date_from=arrow.get())
		Dates(shipment_date_to=arrow.get())
		Dates(shipment_date_from=arrow.get(), shipment_date_to=arrow.get())

		with pytest.raises(ValidationError, match="Shipment date from cannot be greater than shipment date to"):
			Dates(shipment_date_from=arrow.get("2026-01-10"), shipment_date_to=arrow.get("2026-01-01"))

		with pytest.raises(ValidationError, match="Shipment date interval must be less than 30 days"):
			Dates(shipment_date_from=arrow.get("2026-01-01"), shipment_date_to=arrow.get("2026-06-01"))

	def test_validate_update_dates(self):
		Dates(update_date_from=arrow.get())
		Dates(update_date_to=arrow.get())
		Dates(update_date_from=arrow.get(), update_date_to=arrow.get())

		with pytest.raises(ValidationError, match="Update date from cannot be greater than update date to"):
			Dates(update_date_from=arrow.get("2026-01-10"), update_date_to=arrow.get("2026-01-01"))

		with pytest.raises(ValidationError, match="Update date interval must be less than 30 days"):
			Dates(update_date_from=arrow.get("2026-01-01"), update_date_to=arrow.get("2026-06-01"))

	def test_serialize_optional_dates(self):
		assert Dates().serialize_optional_dates(None) is None
		assert Dates().serialize_optional_dates(arrow.get("2026-01-01T12:30:30")) == "2026-01-01"

	def test_serialize_optional_datetimes(self):
		assert Dates().serialize_optional_datetimes(None) is None
		assert Dates().serialize_optional_datetimes(arrow.get("2026-01-01T12:30:30Z")) == "2026-01-01T12:30:30Z"
		assert Dates().serialize_optional_datetimes(arrow.get("2026-01-01T12:30:30+03:00")) == "2026-01-01T09:30:30Z"


class TestOrderDeliveryDates:
	def test_validate_optional_time(self):
		assert OrderDeliveryDates.validate_optional_time(None) is None
		assert OrderDeliveryDates.validate_optional_time("00:00:00") == datetime.time(0, 0, 0)
		assert OrderDeliveryDates.validate_optional_time("12:30:54") == datetime.time(12, 30, 54)

	def test_validate_optional_date(self):
		assert OrderDeliveryDates.validate_optional_date(None) is None
		assert OrderDeliveryDates.validate_optional_date("2026-01-01") == arrow.get(2026, 1, 1)
		assert OrderDeliveryDates.validate_optional_date("2026-01-01T12:30:30") == arrow.get(2026, 1, 1, 12, 30, 30)

	def test_validate_date(self):
		assert OrderDeliveryDates.validate_date("2026-01-01") == arrow.get(2026, 1, 1)
		assert OrderDeliveryDates.validate_date("2026-01-01T12:30:30") == arrow.get(2026, 1, 1, 12, 30, 30)


class TestOrderPickupDelivery:
	def test_validate_optional_date(self):
		assert OrderPickupDelivery.validate_optional_date(None) is None
		assert OrderPickupDelivery.validate_optional_date("2026-01-01") == arrow.get(2026, 1, 1)
		assert OrderPickupDelivery.validate_optional_date("2026-01-01T12:30:30") == arrow.get(2026, 1, 1, 12, 30, 30)


class TestOrderShipment:
	def test_validate_date(self):
		assert OrderShipment.validate_date("2026-01-01") == arrow.get(2026, 1, 1)
		assert OrderShipment.validate_date("2026-01-01T12:30:30") == arrow.get(2026, 1, 1, 12, 30, 30)

	def test_validate_optional_time(self):
		assert OrderShipment.validate_optional_time(None) is None
		assert OrderShipment.validate_optional_time("00:00:00") == datetime.time(0, 0, 0)
		assert OrderShipment.validate_optional_time("12:30:54") == datetime.time(12, 30, 54)


class TestOrder:
	def test_validate_datetimes(self):
		assert Order.validate_datetimes("2026-01-01T12:30:30") == arrow.get(2026, 1, 1, 12, 30, 30)

	def test_validate_optional_datetimes(self):
		assert Order.validate_optional_datetimes(None) is None
		assert Order.validate_optional_datetimes("2026-01-01T12:30:30") == arrow.get(2026, 1, 1, 12, 30, 30)
