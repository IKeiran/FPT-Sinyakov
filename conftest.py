import pytest
from fixture.application import Application
from fixture.db import DBFixture
import json
import os.path
import importlib
import jsonpickle

fixture = None
target = None

@pytest.fixture
def app(request):
    global fixture
    browser = request.config.getoption('--browser')
    web_config = load_config(request.config.getoption('--target'))['web']
    if (fixture is None) or (not fixture.is_valid()):
        fixture = Application(browser, web_config["baseUrl"])
    fixture.session.ensure_login(username=web_config["username"], userpassword=web_config["password"])
    return fixture


@pytest.fixture(scope='session')
def db(request):
    db_config = load_config(request.config.getoption('--target'))['db']
    db_fixture = DBFixture(host=db_config["host"], name=db_config["name"],
                           user=db_config["user"], password=db_config["password"])
    def stop():
        db_fixture.destroy()
    request.addfinalizer(stop)
    return db_fixture


def load_config(file):
    global target
    if target is None:
        config_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), file)
        with open(config_file) as f:
            target = json.load(f)
    return target


def pytest_addoption(parser):
    parser.addoption('--browser', action='store', default='firefox')
    parser.addoption('--target', action='store', default='target.json')


def pytest_generate_tests(metafunc):
    for fixture in metafunc.fixturenames:
        if fixture.startswith('data_'):
            testdata = load_from_module(fixture[5:])
            metafunc.parametrize(fixture, testdata, ids=[str(x) for x in testdata])
        elif fixture.startswith('json_'):
            testdata = load_from_json(fixture[5:])
            metafunc.parametrize(fixture, testdata, ids=[str(x) for x in testdata])


def load_from_module(module):
    return importlib.import_module("data.%s" % module).testdata


def load_from_json(file):
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "data/%s.json" % file)) as data_file:
        return jsonpickle.decode(data_file.read())
    # return importlib.import_module("data.%s" % module).testdata