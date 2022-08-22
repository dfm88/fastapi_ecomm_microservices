# Import all the models, so that Base has them before being
# imported by Alembic
from customers.db.base_class import Base  # noqa
from customers.models.customer import Address, Customer  # noqa
