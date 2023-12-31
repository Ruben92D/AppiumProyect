import pytest
@pytest.fixture(scope="module")
def beforeClass():
    print("Before a class")
    yield
    print("After class")
@pytest.fixture()
def beforeMethod():
    print("Before a method")
    yield
    print("After method")

def test_methodA(beforeClass, beforeMethod):
    print("This is method A")

def test_methodB(beforeClass, beforeMethod):
    print("This is method B")