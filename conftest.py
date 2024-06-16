import pytest
from selene import browser


@pytest.fixture()
def set_browser():
    browser.config.window_width = 1366
    browser.config.window_height = 768
    browser.open('')
    yield
    browser.close()


@pytest.fixture()
def login(set_browser):
    #авторизация
    pass