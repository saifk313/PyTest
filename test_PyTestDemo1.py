import pytest


@pytest.fixture()
def login():
    print("Login before execution")


def test_TestMethod1(login):
    print("This is test method 1")


def test_TestMethod2(login):
    print("This is test method 2")
