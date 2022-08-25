from fastapi import APIRouter

from customers.api.endpoints.api_v1 import customers

router = APIRouter()

# customers
router.include_router(
    customers.customer_router,
    prefix="/customers",
    tags=["customers"]
)
