from email.policy import default
from enum import unique
from typing import Collection

from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from customers.db.base_class import Base


class Customer(Base):
    id = Column(Integer, primary_key=True, index=True)
    full_name = Column(String, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    is_active = Column(Boolean(), default=True)
    is_superuser = Column(Boolean(), default=False)
    addresses = relationship("Address", back_populates='customer')


class Address(Base):
    id = Column(Integer, primary_key=True, index=True)
    street = Column(String(256), nullable=True)
    city = Column(String(256), nullable=True)
    postal_code = Column(String(16), nullable=True)
    country = Column(String(256), nullable=True)
    customer_id = Column(Integer, ForeignKey("customer.id"))
