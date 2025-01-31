

from crud import (
    create_shipment,
    delete_shipment,
    get_shipment,
    get_shipments,
    update_shipment,
)
from database import SessionLocal, get_db
from fastapi import APIRouter, Depends, HTTPException
from schemas import OceanShipmentCreate, OceanShipmentResponse, OceanShipmentUpdate
from sqlalchemy.orm import Session

router = APIRouter()


@router.get("/shipments/", response_model=list[OceanShipmentResponse])
def read_all_shipments(db: Session = Depends(get_db)):
    db_shipments = get_shipments(db)

    if db_shipments is None:
        raise HTTPException(
            status_code=404,
            detail="Não há nenhum embarque na base!",
        )
    return db_shipments


@router.get("/shipments/{shipment_name}", response_model=OceanShipmentResponse)
def read_one_shipment(shipment_name: str, db: Session = Depends(get_db)):
    db_shipment = get_shipment(db=db, shipment_id=shipment_name)

    if db_shipment is None:
        raise HTTPException(
            status_code=404,
            detail="Esse Número de HBL não existe ou não foi criado!",
        )
    return db_shipment


@router.post("/shipments/", response_model=OceanShipmentResponse)
def create_shipment_route(shipment: OceanShipmentCreate, db: Session = Depends(get_db)):
    return create_shipment(shipment=shipment, db=db)


@router.delete("/shipments/{shipment_name}", response_model=OceanShipmentResponse)
def delete_shipment_route(shipment_name: str, db: Session = Depends(get_db)):
    db_shipment = delete_shipment(shipment_id=shipment_name, db=db)

    if db_shipment is None:
        raise HTTPException(
            status_code=404,
            detail="Esse Número de HBL não existe ou não foi criado!",
        )
    return db_shipment


@router.put("/shipments/{shipment_name}", response_model=OceanShipmentResponse)
def update_shipment_route(
    shipment_name: str, shipment: OceanShipmentUpdate, db: Session = Depends(get_db)
):
    db_shipment = update_shipment(shipment_id=shipment_name, shipment=shipment, db=db)

    if db_shipment is None:
        raise HTTPException(
            status_code=404, detail="Esse número de HBL não está cadastrado!",
        )

    return db_shipment
