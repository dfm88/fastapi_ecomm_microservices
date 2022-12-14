from fastapi import APIRouter

from customers.api.endpoints.api_v1 import auth, customers

router = APIRouter()

# customers
router.include_router(
    customers.customer_router,
    prefix="/customers",
    tags=["customers"]
)

# auth
router.include_router(
    auth.auth_router,
    prefix="/auth",
    tags=["login"]
)
