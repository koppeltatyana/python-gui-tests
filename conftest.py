import pytest
from fixture.application import Application


@pytest.fixture(scope="session")  # scope=session создает фиктуру одну на все тесты
def app(request):
    fixture = Application("D:\\AddressBook\\AddressBook.exe")
    request.addfinalizer(fixture.destroy)
    return fixture
