import pytest
from fixture.application import Application
import importlib
import win32com.client
import os


@pytest.fixture(scope="session")  # scope=session создает фиктуру одну на все тесты
def app(request):
    fixture = Application("D:\\AddressBook\\AddressBook.exe")
    request.addfinalizer(fixture.destroy)
    return fixture


def pytest_generate_tests(metafunc):  # функция для генерации тестов
    for fixture in metafunc.fixturenames:  # пробегаем по всем параметрам
        if fixture.startswith("data_"):
            test_data = load_from_module(fixture[5:])
            metafunc.parametrize(fixture, test_data, ids=[str(x) for x in test_data])
        elif fixture.startswith("xlsx_"):
            test_data = load_from_xlsx(fixture[5:])
            metafunc.parametrize(fixture, test_data, ids=[str(x) for x in test_data])


def load_from_module(module):  # берет из модуля данные
    return importlib.import_module("data.{0}".format(module)).test_data


def load_from_xlsx(file):
    excel = win32com.client.Dispatch("Excel.Application")
    wb = excel.Workbooks.Open(
        os.path.join(os.path.dirname(os.path.abspath(__file__)), "data/{}.xlsx".format(file)))
    sheet = wb.ActiveSheet
    data_from_file = [row[0].value for row in sheet.Range("A1:A10")]
    test_data = []
    for gr in data_from_file:
        if gr is None:
            test_data += [""]
        else:
            test_data += [gr]
    return test_data
    excel.Quit()
