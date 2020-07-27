import time

import allure
from hamcrest import assert_that, equal_to, greater_than
from selenium.webdriver import ActionChains

from constants import URL, URL_TRUCKS
from locators import *


@allure.feature('Тестовое задание.')
@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Тест 1.")
def test_1(new_environment):
    driver = new_environment

    with allure.step("1. Перейти на сайт:" + URL):
        driver.get(URL)

    with allure.step("2. Нажать на вкладку 'Транспорт'."):
        driver.find_element(*MainPageLocators.TRUCKS).click()

    with allure.step("3. Убедиться что произошел переход на страницу:" + URL_TRUCKS):
        assert_that(driver.current_url, equal_to(URL_TRUCKS), 'Неверный адрес страницы!')

    with allure.step("4. В форме поиска в поле 'Откуда' написать 'Беларусь'."):
        time.sleep(1)
        driver.find_element(*TrucksPageLocators.INPUT_FROM).send_keys('Беларусь')

    with allure.step("5. Выбрать из выпадающего списка пункт 'Беларусь'"):
        time.sleep(1)
        driver.find_element(*TrucksPageLocators.DROPDOWN_MENU_FROM).click()

    with allure.step("6. В форме поиска в поле 'Куда' написать 'Россия'."):
        driver.find_element(*TrucksPageLocators.INPUT_TO).send_keys('Россия')

    with allure.step("7. Выбрать из выпадающего списка пункт 'Россия'."):
        time.sleep(1)
        driver.find_element(*TrucksPageLocators.DROPDOWN_MENU_TO).click()

    with allure.step("8. Нажать на кнопку 'Найти транспорт'."):
        time.sleep(1)
        button_search = driver.find_element(*TrucksPageLocators.BUTTON_SEARCH_TRUCKS)
        driver.execute_script("window.scrollTo(0,300);")
        ActionChains(driver).move_to_element(button_search).perform()
        button_search.click()

    with allure.step("9. Убедиться что появились результаты поисковой выдачи."):
        time.sleep(2)
        search_results = driver.find_elements(*TrucksPageLocators.SEARCH_RESULTS)
        assert_that(search_results.__len__(), greater_than(0), "Нет результатов поиска!")

    with allure.step(
            "10. Нажать на последней карточке поисковой выдачи (в конце страницы) по кнопке 'ПОКАЗАТЬ КОНТАКТЫ'."):
        button_open_contacts = driver.find_element(*TrucksPageLocators.SHOW_CONTACTS)
        driver.execute_script("window.scrollTo(0,2500);")
        ActionChains(driver).move_to_element(button_open_contacts).click().perform()

    with allure.step("11. Убедиться что появился попап регистрации пользователя."):
        time.sleep(1)
        pop_up_fast_reg = driver.find_element(*TrucksPageLocators.POP_UP_FAST_REG)
        driver.switch_to.frame(pop_up_fast_reg)
        pop_up_title = driver.find_element(*TrucksPageLocators.POPUP_FAST_REG_TITLE)
        assert_that(pop_up_title.is_displayed(), equal_to(True), "Попап регистрации не появился!")
