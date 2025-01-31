from sqlalchemy import Column, DateTime, Float, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from database import Base


class OceanShipmentModel(Base):
    __tablename__ = "shipments"

    id = Column(Integer, primary_key=True)
    hbl_number = Column(String, unique=True, nullable=False)
    mbl_number = Column(String)
    shipper = Column(String, nullable=False)
    consignee = Column(String, nullable=False)
    notify = Column(String, nullable=False)
    pol = Column(String, nullable=False)
    vessel_origin = Column(String, nullable=False)
    vessel_voyage = Column(String, nullable=False)
    number_of_packages = Column(Integer, nullable=False)
    type_of_packages = Column(String, nullable=False)
    material_description = Column(String, nullable=False)
    gross_weight = Column(Float, nullable=False)
    measurement_cbm = Column(Float, nullable=False)
    on_board_date = Column(DateTime, nullable=False)
    issue_date = Column(DateTime, nullable=False)
    created_at = Column(DateTime(timezone=True), default=func.now())

    containers = relationship(
        "ContainerModel", back_populates="shipment", cascade="all, delete-orphan",
    )

    freight = relationship("OceanFreightModel", uselist=False, back_populates="shipment")


class ContainerModel(Base):
    __tablename__ = "containers"

    id = Column(Integer, primary_key=True)
    container_number = Column(String, unique=True, nullable=False)
    container_type = Column(String, nullable=False)
    ncm = Column(String, nullable=False)
    un = Column(String)

    shipment_id = Column(Integer, ForeignKey("shipments.id"), nullable=False)
    shipment = relationship("OceanShipmentModel", back_populates="containers")


class OceanFreightModel(Base):
    __tablename__ = "freights"

    id = Column(Integer, primary_key=True)
    ocean_freight = Column(Float, nullable=False)
    ocean_freight_currency = Column(String, nullable=False)
    terminal_handling = Column(Float, nullable=False)
    terminal_handling_currency = Column(String, nullable=False)
    documentation_fee = Column(Float, nullable=False)
    documentation_fee_currency = Column(String, nullable=False)
    tax_4th = Column(Float)
    tax_4th_currency = Column(String)
    tax_5th = Column(Float)
    tax_5th_currency = Column(String)
    tax_6th = Column(Float)
    tax_6th_currency = Column(String)
    tax_7th = Column(Float)
    tax_7th_currency = Column(String)
    tax_8th = Column(Float)
    tax_8th_currency = Column(String)
    tax_9th = Column(Float)
    tax_9th_currency = Column(String)
    tax_10th = Column(Float)
    tax_10th_currency = Column(String)
    tax_11th = Column(Float)
    tax_11th_currency = Column(String)
    tax_12th = Column(Float)
    tax_12th_currency = Column(String)
    tax_13th = Column(Float)
    tax_13th_currency = Column(String)
    tax_14th = Column(Float)
    tax_14th_currency = Column(String)
    tax_15th = Column(Float)
    tax_15th_currency = Column(String)

    shipment_id = Column(Integer, ForeignKey("shipments.id"), nullable=False)
    shipment = relationship("OceanShipmentModel", back_populates="freight")
