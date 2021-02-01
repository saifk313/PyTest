import pytest


@pytest.fixture()
def loginout():
    print("Login before execution")
    yield
    print("Logout after execution")


def test_TestMethod1():
    print("This is test method 1")


def test_TestMethod2(loginout):
    print("This is test method 2")