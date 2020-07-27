import allure
import pytest

from selenium import webdriver


@pytest.fixture(scope='session')
def new_environment():
    with allure.step('Открытие браузера Google Chrome.'):
        driver = webdriver.Chrome('./chromedriver')
        driver.fullscreen_window()

    yield driver
    with allure.step("Закрыть вкладку"):
        driver.close()

    with allure.step("Закрыть браузер"):
        driver.quit()

