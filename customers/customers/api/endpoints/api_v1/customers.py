from typing import Any

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from customers.api.deps.db import get_db
from customers.schemas.custumer_schema import CustomerCreate
from customers.services.customer_service import CustomerService

customer_router = APIRouter()


@customer_router.post('/create')
async def create_customer(
    data: CustomerCreate,
    db: Session = Depends(get_db),
) -> Any:
    user = CustomerService.create(db, data)
    return user
