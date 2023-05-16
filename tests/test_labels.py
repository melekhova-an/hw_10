import allure
from allure_commons.types import Severity


def test_dynamic_labels():
    allure.dynamic.tag("web")
    allure.dynamic.severity(Severity.BLOCKER)
    allure.dynamic.feature("Пуллреквесты в репозитории")
    allure.dynamic.story("Неавторизованный пользователь может просмотреть пуллреквесты в репозитории")
    allure.dynamic.link("https://github.com", name="Testing")
    pass


@allure.tag("web")
@allure.severity(Severity.CRITICAL)
@allure.label("owner", "an-melekhova")
@allure.feature("Пуллреквесты в репозитории")
@allure.story("Неавторизованный пользователь может просмотреть пуллреквесты в репозитории")
@allure.link("https://github.com", name="Testing")
def test_decorator_labels():
    pass
