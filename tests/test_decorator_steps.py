import allure
from selene.support import by
from selene.support.shared import browser
from selene.support.shared.jquery_style import s

def test_decorator_steps():
    open_main_page()
    search_for_repository("melekhova-an/python_hw_3")
    go_to_repository("melekhova-an/python_hw_3")
    open_branch_tab()
    should_see_branch_with_name("Firtstbranch")

@allure.step("Открываем главную страницу")
def open_main_page():
    browser.open("https://github.com")


@allure.step("Ищем репозиторий {repo}")
def search_for_repository(repo):
    s(".header-search-input").click()
    s(".header-search-input").send_keys(repo)
    s(".header-search-input").submit()


@allure.step("Переходим по ссылке репозитория {repo}")
def go_to_repository(repo):
    s(by.link_text(repo)).click()


@allure.step("Открываем таб Pull requests")
def open_branch_tab():
    s("#pull-requests-tab").click()

@allure.step("Проверяем наличие бранча с названием {name}")
def should_see_branch_with_name(name):
    s(by.partial_text(name)).click()