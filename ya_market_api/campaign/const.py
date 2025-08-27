from enum import Enum


class APIAvailabilityStatus(Enum):
	AVAILABLE = "AVAILABLE"
	DISABLED_BY_INACTIVITY = "DISABLED_BY_INACTIVITY"


class PlacementType(Enum):
	FBS = "FBS"
	FBY = "FBY"
	DBS = "DBS"
