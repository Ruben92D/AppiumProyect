import pytest


@pytest.fixture(scope="module")
def beforeClass():
    print("beforeClass en conftest")
    yield
    print("beforeClass en conftest")
@pytest.fixture()
def beforeMethod():
    print("beforeMethod en confest")