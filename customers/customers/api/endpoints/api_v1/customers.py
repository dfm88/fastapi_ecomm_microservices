from typing import Any

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from customers.api.deps.db import get_db
from customers.schemas.custumer_schema import CustomerCreate, CustomerOut, CustomerUpdate
from customers.services.customer_service import CustomerService

customer_router = APIRouter()


@customer_router.post('/create')
async def create_customer(
    data: CustomerCreate,
    db: Session = Depends(get_db),
) -> Any:
    user = CustomerService.create(db, data)
    return user


@customer_router.put("/edit/{id}", response_model=CustomerOut, status_code=200)
async def update_customer(
    *,
    db: Session = Depends(get_db),
    id: int,
    customer_in: CustomerUpdate
) -> Any:
    customer = CustomerService.get_by_id(db, id)
    if not customer:
        return HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User with id {id} does not exists"
        )
    customer = CustomerService.update(
        db=db,
        db_obj=customer,
        obj_in=customer_in
    )
    return customer
