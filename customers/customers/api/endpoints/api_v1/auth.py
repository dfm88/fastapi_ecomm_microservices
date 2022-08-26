from typing import Any

from fastapi import APIRouter, Body, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from jose import jwt
from pydantic import ValidationError
from sqlalchemy.orm import Session

from customers.api.deps.customer import get_current_active_customer
from customers.api.deps.db import get_db
from customers.core import security
from customers.core.config import settings
from customers.models.customer import Customer
from customers.schemas.custumer_schema import CustomerOut
from customers.schemas.token_schema import TokenPayload, TokenSchema
from customers.services.customer_service import CustomerService

auth_router = APIRouter()


@auth_router.post(
    '/login',
    summary="Create access and refresh tokens for user",
    response_model=TokenSchema
)
async def login(
    db: Session = Depends(get_db),
    form_data: OAuth2PasswordRequestForm = Depends()
) -> Any:
    user = CustomerService.authenticate(
        db=db,
        email=form_data.username,
        password=form_data.password
    )
    if not user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Incorrect email or password"
        )
    elif not CustomerService.is_active(user):
        raise HTTPException(status_code=400, detail="Inactive user")

    # create access and refresh tokens
    return {
        "access_token": security.create_token(user.id),
        "refresh_token": security.create_token(user.id, refresh=True),
    }


@auth_router.post(
    '/test-token',
    summary="Test if the access token is ok",
    response_model=CustomerOut
)
async def test_token(user: Customer = Depends(get_current_active_customer)):
    """
    First authenticated endpoint
    """
    return user


@auth_router.post('/refresh', summary="Refresh token", response_model=TokenSchema)
async def refresh_token(
    db: Session = Depends(get_db),
    refresh_token: str = Body(...)
):
    try:
        payload = jwt.decode(
            token=refresh_token,
            key=settings.JWT_SECRET_KEY_REFRESH,
            algorithms=[settings.ALGORITHM]
        )
        token_data = TokenPayload(**payload)
    except (jwt.JWTError, ValidationError):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Invalid token",
            headers={"WWW-Authenticate": "Bearer"},
        )
    user = CustomerService.get_by_id(db, token_data.sub)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Invalid token for user",
        )
    return {
        "access_token": security.create_token(user.id),
        "refresh_token": security.create_token(user.id, refresh=True),
    }

# TODO reset password & recover password
