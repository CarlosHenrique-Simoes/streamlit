from models import OceanShipmentModel
from schemas import OceanShipmentCreate, OceanShipmentUpdate
from sqlalchemy.orm import Session


def get_shipments(db: Session):
    return db.query(OceanShipmentModel).all()


def get_shipment(db: Session, shipment_id: str):
    return (
        db.query(OceanShipmentModel)
        .filter(OceanShipmentModel.hbl_number == shipment_id)
        .first()
    )

def create_shipment(db: Session, shipment: OceanShipmentCreate):
    db_shipment = OceanShipmentModel(**shipment.model_dump())
    db.add(db_shipment)
    db.commit()
    db.refresh(db_shipment)
    return db_shipment

def delete_shipment(db: Session, shipment_id: str):
    db_shipment = (
        db.query(OceanShipmentModel)
        .filter(OceanShipmentModel.hbl_number == shipment_id)
        .first()
    )
    db.delete(db_shipment)
    db.commit()
    return db_shipment


def update_shipment(db: Session, shipment_id: str, shipment: OceanShipmentUpdate):
    db_shipment = (
        db.query(OceanShipmentModel)
        .filter(OceanShipmentModel.hbl_number == shipment_id)
        .first()
    )

    if db_shipment is None:
        return None

    if shipment.hbl_number is not None:
        db_shipment.hbl_number = shipment.hbl_number

    if shipment.mbl_number is not None:
        db_shipment.mbl_number = shipment.mbl_number

    if shipment.shipper is not None:
        db_shipment.shipper = shipment.shipper

    if shipment.consignee is not None:
        db_shipment.consignee = shipment.consignee

    if shipment.notify is not None:
        db_shipment.notify = shipment.notify

    if shipment.pol is not None:
        db_shipment.pol = shipment.pol

    if shipment.vessel_origin is not None:
        db_shipment.vessel_origin = shipment.vessel_origin

    if shipment.vessel_voyage is not None:
        db_shipment.vessel_voyage = shipment.vessel_voyage

    if shipment.number_of_packages is not None:
        db_shipment.number_of_packages = shipment.number_of_packages

    if shipment.type_of_packages is not None:
        db_shipment.type_of_packages = shipment.type_of_packages

    if shipment.material_description is not None:
        db_shipment.material_description = shipment.material_description

    if shipment.gross_weight is not None:
        db_shipment.gross_weight = shipment.gross_weight

    if shipment.measurement_cbm is not None:
        db_shipment.measurement_cbm = shipment.measurement_cbm

    if shipment.on_board_date is not None:
        db_shipment.on_board_date = shipment.on_board_date

    if shipment.issue_date is not None:
        db_shipment.issue_date = shipment.issue_date

    db.commit()
    db.refresh(db_shipment)
    return db_shipment
