from selene.support.shared import browser
from selene import be, have


def test_finds_selene():
    browser.config.hold_browser_open = True
    browser.open('/ncr').should(have.title('Google'))
    browser.element('[name="q"]').should(be.blank).set_value('selene').press_enter()
    browser.element('#search').should(have.text('yashaka/selene: User-oriented Web UI browser'))

    results = browser.all('#rso>div')
    results.should(have.size_greater_than(6))

def test_finds_selene_with_refined_query():
    browser.config.hold_browser_open = True
    browser.open('/ncr').should(have.title('Google'))
    browser.element('[name="q"]').should(be.blank).set_value('selene').press_enter()
    browser.element('#search').should(have.text('yashaka/selene: User-oriented Web UI browser'))

    results = browser.all('#rso>div')
    results.should(have.size_greater_than(6))

    browser.element('[name="q"]').type(' yashaka github').press_enter()
    results.first.element('h3').click()
    browser.should(have.title_containing('yashaka/selene'))

browser.quit()
