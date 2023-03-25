from selene.support.shared import browser
from selene import be, have
from selenium.webdriver import ActionChains


def test_google_search():
    browser.config.timeout = 10
    browser.open('https://google.com')
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('#search').should(have.text('Selene - User-oriented Web UI browser tests in Python'))
    browser.all('#search .g').with_(timeout=20).should(have.size_greater_than(5))
    browser.should(have.title('selene'))

#browser.driver - вызов селениeм веб драйвер
#ActionChains(browser.driver).click_and_hold() - вызов библиотеки ActionChains селениума, через точку можно вызывать всякие функции типа click_and_hold
ActionChains(browser.driver).move_to_element(browser.element('#super-button').get_actual_webelement()).drag_and_drop(browser.element('#area'))
ActionChains(browser.driver).move_to_element(browser.element('#super-button')()).drag_and_drop(browser.element('#area')()).perform()
#() == .get_actual_webelement()