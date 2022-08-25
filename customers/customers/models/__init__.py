# Import all the models, so that models.py won't crash on queries
from customers.models.customer import Customer  # noqa
from customers.models.address import Address  # noqa
