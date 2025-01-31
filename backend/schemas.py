from datetime import datetime
from enum import Enum
from typing import Optional

from pydantic import BaseModel, PositiveFloat, PositiveInt


class OceanShipmentBase(BaseModel):

    hbl_number: str
    mbl_number: str
    shipper: str
    consignee: str
    notify: str
    pol: str
    vessel_origin: str
    vessel_voyage: str
    number_of_packages: PositiveInt
    type_of_packages: str
    material_description: str
    gross_weight: PositiveFloat
    measurement_cbm: PositiveFloat
    on_board_date: datetime
    issue_date: datetime

class OceanShipmentCreate(OceanShipmentBase):
    pass

class OceanShipmentResponse(OceanShipmentBase):

    id: int
    created_at: datetime

    class Config:
        from_attributes = True

class OceanShipmentUpdate(BaseModel):

    hbl_number: Optional[str] = None
    mbl_number: Optional[str] = None
    shipper: Optional[str] = None
    consignee: Optional[str] = None
    notify: Optional[str] = None
    pol: Optional[str] = None
    vessel_origin: Optional[str] = None
    vessel_voyage: Optional[str] = None
    number_of_packages: Optional[PositiveInt] = None
    type_of_packages: Optional[str] = None
    material_description: Optional[str] = None
    gross_weight: Optional[PositiveFloat] = None
    measurement_cbm: Optional[PositiveFloat] = None
    on_board_date: Optional[datetime] = None
    issue_date: Optional[datetime] = None
