from selenium.webdriver.support.ui import Select
import allure


class BudgetPage:
    driver = None

    def __init__(self, driver):
        self.driver = driver

    @allure.step
    def open(self):
        self.driver.get("http://127.0.0.1:3000/")
        return self

    @allure.step
    def select_category(self, category):
        select_category = Select(self.driver.find_element_by_name('categoryId'))
        return select_category.select_by_visible_text(category)

    @allure.step
    def add_description(self, description):
        add_description = self.driver.find_element_by_name('description')
        return add_description.send_keys(description)

    @allure.step
    def add_value(self, value):
        add_value = self.driver.find_element_by_name('value')
        return add_value.send_keys(value)

    @allure.step
    def btn_submit(self):
        return self.driver.find_element_by_css_selector('button.submit')

    @allure.step
    def btn_cancel(self):
        return self.driver.find_element_by_css_selector('button.cancel')

    @allure.step
    def btn_delete(self):
        return self.driver.find_element_by_css_selector('button.delete')

    @allure.step
    def cell_value(self, number):
        return self.driver.find_element_by_css_selector(f':nth-child({number}) > ._3XkHf > ._3-t-g')

    @allure.step
    def row(self, number):
        return self.driver.find_element_by_css_selector(f'tbody > :nth-child({number})')

    @allure.step
    def working_balance(self):
        return self.driver.find_element_by_css_selector('*:nth-child(5)>._3S2Fs>.sG1fB')

