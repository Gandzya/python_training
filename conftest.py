import pytest

from fixture.application import Application

fixture = None


@pytest.fixture
def app(request):
    global fixture

    if fixture is None:
        browser = request.config.getoption("--browser")
        base_url = request.config.getoption("--baseUrl")
        fixture = Application()
        fixture.session.login(username="admin", password="secret")
    else:
        if not fixture.is_valid():
            pass
    return fixture


@pytest.fixture(scope="session", autouse=True)
def stop(request):
    def finish():
        fixture.session.ensure_logout()
        fixture.destroy()

    request.addfinalizer(finish)
    return fixture


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="firefox")
    parser.addoption("--baseUrl", action="store", default="http://localhost/addressbook")
