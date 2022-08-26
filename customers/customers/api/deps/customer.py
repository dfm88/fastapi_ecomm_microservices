from datetime import datetime

from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import jwt
from pydantic import ValidationError
from sqlalchemy.orm import Session

from customers.api.deps.db import get_db
from customers.core.config import settings
from customers.models.customer import Customer
from customers.schemas.token_schema import TokenPayload
from customers.services.customer_service import CustomerService

reuseable_oauth = OAuth2PasswordBearer(
    tokenUrl=f"{settings.API_V1_STR}/auth/login",
    scheme_name="JWT"
)


async def get_current_customer(
    db: Session = Depends(get_db),
    token: str = Depends(reuseable_oauth)
) -> Customer:
    try:
        payload = jwt.decode(
            token=token,
            key=settings.JWT_SECRET_KEY,
            algorithms=[settings.ALGORITHM]
        )
        token_data = TokenPayload(**payload)

        if datetime.fromtimestamp(token_data.exp) < datetime.now():
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Token expired",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except (jwt.JWTError, ValidationError):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Could not validate credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )

    customer = CustomerService.get_by_id(
        db=db,
        id=token_data.sub
    )

    if not customer:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Could not find customer",
        )

    return customer


def get_current_active_customer(
    current_customer: Customer = Depends(get_current_customer),
) -> Customer:
    if not CustomerService.is_active(current_customer):
        raise HTTPException(status_code=400, detail="Inactive customer")
    return current_customer


def get_current_active_superuser(
    current_customer: Customer = Depends(get_current_customer),
) -> Customer:
    if not CustomerService.is_superuser(current_customer):
        raise HTTPException(
            status_code=400, detail="The user doesn't have enough privileges"
        )
    return current_customer
