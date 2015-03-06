# -*- coding: utf-8 -*-
import random, pytest
from model.group import Group
from fixture.application import Application

@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_group(app):
    app.login_as("admin", "secret")
    test_group = Group("Friends" + str(random.randint(0,1000000)), "My friends", "for current time")
    app.add_new_group(test_group)
    app.logout()