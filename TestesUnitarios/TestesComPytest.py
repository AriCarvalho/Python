import pytest


#pytest --fixtures
@pytest.fixture()
def resource():
    return 1


def test_a(resource, tmpdir):
    print("teste A:" + str(tmpdir))
    assert 1 == resource


def test_b():
    assert 1 == 2


def test_c():
    assert 1 == 2
