from pydantic import EmailStr
from sqlalchemy.orm import Session

from customers.core.security import get_password_hash, verify_password
from customers.models.customer import Customer
from customers.schemas.custumer_schema import CustomerCreate


class CustomerService:

    @staticmethod
    def create(db: Session, customer: CustomerCreate) -> Customer:
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

    @staticmethod
    def authenticate(db: Session, email: EmailStr, password: str) -> Customer | None:
        user: Customer = CustomerService.get_by_email(db=db, email=email)
        if not user:
            return None
        if not verify_password(
            password=password,
            hashed_password=user.hashed_password
        ):
            return None
        return user

    @staticmethod
    def get_by_email(db: Session, email: EmailStr) -> Customer | None:
        return db.query(Customer).filter(Customer.email == email).first()

    @staticmethod
    def get_by_id(db: Session, id: int) -> Customer | None:
        return db.query(Customer).filter(Customer.id == id).first()

    @staticmethod
    def is_active(user: Customer) -> bool:
        return user.is_active

    @staticmethod
    def is_superuser(user: Customer) -> bool:
        return user.is_superuser
