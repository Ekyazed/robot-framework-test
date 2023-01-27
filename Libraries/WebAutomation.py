from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from robot.api.deco import keyword
from robot.api.logger import info
import pandas as pd


class WebAutomation:
    ROBOT_LIBRARY_SCOPE = "GLOBAL"

    def __init__(self):
        self._service = Service("../service/chromedriver.exe")
        self._chrome_option = Options()
        self._driver = None
        self._action = ActionChains(self._driver)

    @keyword("Open Chrome Browser")
    def open_chrome_browser(self, url, headless: bool, closeBrowser: bool, maximise_window: bool = True):
        if url is None:
            raise ValueError("An URL must be provided")
        if headless is True:
            self._chrome_option.headless = headless
        if closeBrowser is False:
            self._chrome_option.add_experimental_option("detach", closeBrowser)
        self._driver = webdriver.Chrome(service=self._service, options=self._chrome_option)
        if maximise_window is True:
            self._driver.maximize_window()
        self._driver.get(url)

    @keyword("Pass Through Modal")
    def pass_through_modal(self, Id=None):
        if Id is None:
            raise ValueError("A css class need to be provided")
        else:
            modal_close_button = self._driver.find_element(By.ID, Id)
            self._action.move_to_element(modal_close_button)
            modal_close_button.click()

    @keyword("Input Text")
    def input_text(self, input_name, content, browser: WebDriver = None):
        if input_name is None or content is None:
            raise ValueError("An input name or a content to fill is required")
        else:
            info(self._driver.current_url)
            inputElement = self._driver.find_element(By.ID, input_name)
            inputElement.send_keys(content)

    @keyword("Click Element")
    def click_element(self, elem_id):
        if elem_id is None:
            raise ValueError("An Element should be provided")
        else:
            elem = self._driver.find_element(By.ID, elem_id)
            elem.click()

    @keyword("Submit Form")
    def submit_form(self):
        """Submit a form only if the form is submitted by a button"""
        elem = self._driver.find_element(By.XPATH, "//button[@type='submit']")
        elem.click()

    @keyword("Select From Range")
    def select_from_range(self, Id, value):
        if value is None:
            raise ValueError("A value should be provided")
        else:
            elem = self._driver.find_element(By.ID, Id)
            elem.click()
            listElem = self._driver.find_element(By.XPATH, "//option[@value='" + value + "']")
            listElem.click()

    @keyword("Wait Until Element Appear")
    def wait_until_element_appear(self, Id, timeout=5.0):
        wait = WebDriverWait(self._driver, timeout)
        wait.until(EC.visibility_of_element_located((By.ID, Id)))
        self._driver.save_screenshot("img.png")

    @keyword("Extract Data From Table")
    def extract_data_from_table(self, tableClass):
        web_table = pd.read_html(self._driver.find_element(By.CLASS_NAME, tableClass).get_attribute('outerHTML'))[0]
        web_table.to_excel("try_scrapping.xlsx")
