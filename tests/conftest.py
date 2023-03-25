import pytest
from selene import browser


@pytest.fixture(scope='function', autouse=True)
def browser_management():
    browser.config.timeout = 3.0
    browser.config.base_url = 'https://google.com'
    yield
    browser.quit()