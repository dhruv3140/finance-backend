from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import func
from .. import model, database

router = APIRouter(
    prefix="/dashboard",
    tags=["Dashboard"]
)

# 1. SUMMARY ENDPOINT
@router.get("/summary")
def get_dashboard_summary(db: Session = Depends(database.get_db)):
    records = db.query(model.Record).all()
    total_income = 0.0
    total_expense = 0.0
    for record in records:
        if record.type == "income":
            total_income += record.amount
        elif record.type == "expense":
            total_expense += record.amount

    net_balance = total_income - total_expense
    
    return {
        "total_income": total_income,
        "total_expense": total_expense,
        "net_balance": net_balance
    }
