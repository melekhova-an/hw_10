from selene.support import by
from selene.support.conditions import be
from selene.support.shared import browser
from selene.support.shared.jquery_style import s


def test_github():
    browser.open("https://github.com/")

    s(".header-search-input").click()
    s(".header-search-input").send_keys("melekhova-an/python_hw_3")
    s(".header-search-input").submit()

    s(by.link_text("melekhova-an/python_hw_3")).click()
    s("#pull-requests-tab").click()

    s(by.partial_text("Firtstbranch")).should(be.visible)
