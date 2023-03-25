from selene.support.shared import browser
from selene import be, have
from selenium.webdriver import ActionChains


def test_google_search():
    browser.config.hold_browser_open = True
    browser.open('https://google.com').should(have.title('Google'))
    browser.element('[name="q"]').should(be.blank).set_value('selene').press_enter()
    browser.element('#search').should(have.text('yashaka/selene: User-oriented Web UI browser'))

    results = browser.all('#rso>div')
    results.should(have.size_greater_than(6))

    browser.quit()
