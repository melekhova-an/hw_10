import allure
from selene.support import by
from selene.support.conditions import be
from selene.support.shared import browser
from selene.support.shared.jquery_style import s


def test_dynamic_steps():
    with allure.step("Открываем главную страницу"):
        browser.open("https://github.com")

    with allure.step("Ищем репозиторий"):
        s(".header-search-input").click()
        s(".header-search-input").send_keys("melekhova-an/python_hw_3")
        s(".header-search-input").submit()

    with allure.step("Переходим по ссылке репозитория"):
        s(by.link_text("melekhova-an/python_hw_3")).click()

    with allure.step("Открываем таб Pull requests"):
        s("#pull-requests-tab").click()

    with allure.step("Проверяем наличие бранча с названием Firtstbranch"):
        s(by.partial_text("Firtstbranch")).should(be.visible)






