from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import model, schemas, database
from ..dependencies import require_role  # <-- We import the bouncer here!

router = APIRouter(
    prefix="/records",
    tags=["Records"]
)

@router.post("/", response_model=schemas.RecordResponse, dependencies=[Depends(require_role(["admin", "analyst"]))])
def create_record(record: schemas.RecordCreate, db: Session = Depends(database.get_db)):
    mock_user_id = 1 
    new_record = model.Record(**record.model_dump(), user_id=mock_user_id)
    db.add(new_record)
    db.commit()
    db.refresh(new_record)
    return new_record

@router.get("/", response_model=list[schemas.RecordResponse])
def get_records(db: Session = Depends(database.get_db)):
    return db.query(model.Record).all()

@router.put("/{record_id}", response_model=schemas.RecordResponse)
def update_record(record_id: int, updated_record: schemas.RecordCreate, db: Session = Depends(database.get_db)):
    record = db.query(model.Record).filter(model.Record.id == record_id).first()
    if not record:
        raise HTTPException(status_code=404, detail="Record not found")
    
    for key, value in updated_record.model_dump().items():
        setattr(record, key, value)
    
    db.commit()
    db.refresh(record)
    return record

@router.delete("/{record_id}", status_code=204, dependencies=[Depends(require_role(["admin"]))])
def delete_record(record_id: int, db: Session = Depends(database.get_db)):
    record = db.query(model.Record).filter(model.Record.id == record_id).first()
    if not record:
        raise HTTPException(status_code=404, detail="Record not found")
    
    db.delete(record)
    db.commit()
    return None