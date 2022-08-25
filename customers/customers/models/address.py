from typing import TYPE_CHECKING

from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from customers.db.base_class import Base

if TYPE_CHECKING:
    from customers.models.customer import Customer  # noqa


class Address(Base):
    id = Column(Integer, primary_key=True, index=True)
    street = Column(String(256), nullable=True)
    city = Column(String(256), nullable=True)
    postal_code = Column(String(16), nullable=True)
    country = Column(String(256), nullable=True)
    customer_id = Column(Integer, ForeignKey("customer.id"))
    customer = relationship("Customer", back_populates="addresses")
