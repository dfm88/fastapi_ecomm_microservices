from sqlalchemy.orm import Session

from customers.core.security import get_password_hash
from customers.models.customer import Customer
from customers.schemas.custumer_schema import CustomerCreate


class CustomerService:

    @staticmethod
    def create(db: Session, customer: CustomerCreate):
        db_obj = Customer(
            email=customer.email,
            hashed_password=get_password_hash(customer.password),
            is_superuser=customer.is_superuser,
            full_name=customer.full_name,
            is_active=customer.is_active,
        )

        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj
