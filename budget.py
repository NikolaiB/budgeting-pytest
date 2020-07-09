from selenium.webdriver.chrome.webdriver import WebDriver
from pages.budget_page import BudgetPage
import allure


class TestBudget:

    def setup_method(self):
        self.driver = WebDriver(executable_path="/Users/nikolai/Downloads/chromedriver")
        self.budgetPage = BudgetPage(self.driver)

    @allure.title("Add a new item")
    def test_add_item(self):
        self.budgetPage.open()
        self.budgetPage.select_category('Income')
        self.budgetPage.add_description('Salary')
        self.budgetPage.add_value('1000')
        self.budgetPage.btn_submit().click()
        assert self.budgetPage.cell_value(7).text == '$1,000.00'
        assert self.budgetPage.working_balance().text == '$3,213.93'

    @allure.title("Update existing item")
    def test_update_item(self):
        self.budgetPage.open()
        self.budgetPage.row(6).click()
        self.budgetPage.add_value('0')
        self.budgetPage.btn_submit().click()
        assert self.budgetPage.cell_value(6).text == '$57,000.00'
        assert self.budgetPage.working_balance().text == '$53,513.93'

    @allure.title("Delete an item")
    def test_delete_item(self):
        self.budgetPage.open()
        assert self.budgetPage.working_balance().text == '$2,213.93'
        self.budgetPage.row(5).click()
        self.budgetPage.btn_delete().click()
        assert self.budgetPage.working_balance().text == '$3,313.93'

    def teardown_method(self):
        self.driver.close()