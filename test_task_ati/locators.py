from selenium.webdriver.common.by import By


class MainPageLocators(object):
    """A class for Main Page locators. All locators should come here."""
    TRUCKS = (By.XPATH, "//a[contains(@data-name,'link-transport')]")


class TrucksPageLocators(object):
    """A class for Trucks Page locators. All locators should come here."""
    INPUT_FROM = (By.XPATH, "//input[contains(@id,'from')]")
    DROPDOWN_MENU_FROM = (By.XPATH, "//div[@class='suggestion']")
    INPUT_TO = (By.XPATH, "//input[contains(@id,'to')]")
    DROPDOWN_MENU_TO = (By.XPATH, "(//div[contains(@class,'suggestion')])[1]")
    BUTTON_SEARCH_TRUCKS = (By.XPATH, "//button[contains(.,'найти транспорт')]")
    SEARCH_RESULTS = (By.XPATH, '//*[@id="root"]/main/div[3]/div/div[4]/div')
    SHOW_CONTACTS = (By.XPATH, "(//div[@class='_1n2PI-2-0-485'][contains(.,'Показать контакты')])[10]")
    POPUP_FAST_REG_TITLE = (By.XPATH, "//h1[@class='ati-core-popup-header'][contains(.,'Вход в АТИ')]")
    POP_UP_FAST_REG = (By.XPATH, '//*[@id="root"]/main/iframe')
