from fastapi.testclient import TestClient
from sqlalchemy.orm import Session
from customers.schemas.custumer_schema import CustomerCreate
from customers.services.customer_service import CustomerService

from tests.conftest import settings


def test_get_access_token(test_env, db: Session, client: TestClient) -> None:
    customer_create = CustomerCreate(
        email="example@maipl.com",
        is_active=True,
        password="test",
    )
    created_customer = CustomerService.create(
        db=db,
        customer=customer_create
    )
    login_data = {
        "username": created_customer.email,
        "password": customer_create.password,
    }
    r = client.post(f"{settings.API_V1_STR}/auth/login", data=login_data)
    tokens = r.json()
    assert r.status_code == 200
    assert "access_token" in tokens
    assert tokens["access_token"]


class TestClassBasedExample:

    # better use fixtures and theire scopes
    # check https://docs.pytest.org/en/6.2.x/fixture.html

    # Method level, pre function
    def setup_method(self, db):
        print("setup_method(self):Execute before each test method")

    # Method level, post function
    def teardown_method(self, db):
        print("teardown_method(self):Execute after each test method\n")

    # Class level, pre function
    def setup_class(self):
        print("setup_class(self): Execute once before each test class\n")

    # Class level, post function
    def teardown_class(self):
        print("teardown_class(self): Execute once after each test class")

    # Test case a
    def test_a(self):
        print("test_a method")
        assert True

    # Test case b
    def test_b(self):
        print("test_b method")
        assert True

    def test_get_access_token(test_env, db: Session, client: TestClient) -> None:
        customer_create = CustomerCreate(
            email="example@maipl.com",
            is_active=True,
            password="test",
        )
        created_customer = CustomerService.create(
            db=db,
            customer=customer_create
        )
        login_data = {
            "username": created_customer.email,
            "password": customer_create.password,
        }
        r = client.post(f"{settings.API_V1_STR}/auth/login", data=login_data)
        tokens = r.json()
        assert r.status_code == 200
        assert "access_token" in tokens
        assert tokens["access_token"]


# def test_use_access_token(
#     client: TestClient, superuser_token_headers: Dict[str, str]
# ) -> None:
#     r = client.post(
#         f"{settings.API_V1_STR}/login/test-token", headers=superuser_token_headers,
#     )
#     result = r.json()
#     assert r.status_code == 200
#     assert "email" in result
