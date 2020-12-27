from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.select import Select
from selenium import webdriver
import time

class RoyalBank:
    def __init__(self, username=None, password=None):
        # check if username and password exist
        if username is None or password is None:
            print('bad inputs')
            return

        # create and add options, and initialize web driver
        options = Options()
        options.add_argument("--headless")
        driver = webdriver.Chrome(options=options)

        # run login task
        self.__login(driver, username, password)
        time.sleep(5)
        # run download transactions task
        self.__download_transactions(driver, username, password)
        time.sleep(5)
        # quit selenium
        driver.quit()          

    def __login(self, driver=None, username=None, password=None):
        # get login page
        login_url = 'https://www1.royalbank.com/cgi-bin/rbaccess/rbcgi3m01?F6=1&F7=IB&F21=IB&F22=IB&REQUEST=ClientSignin'
        driver.get(login_url)

        # get xpaths for login page
        username_input = '//*[@id="K1"]'
        password_input = '//*[@id="QQ"]'
        submit = '//*[@id="rbunxcgi"]/fieldset/div[4]/div/button'

        # fill username/password inputs and click submit
        driver.find_element_by_xpath(username_input).send_keys(username)
        driver.find_element_by_xpath(password_input).send_keys(password)
        driver.find_element_by_xpath(submit).click()

    def __download_transactions(self, driver=None, username=None, password=None):
        # get download page
        download_url = 'https://www1.royalbank.com/cgi-bin/rbaccess/rbunxcgi?REQUEST=QuickenDownload&F22=HTPCBINET&LANGUAGE=ENGLISH'
        driver.get(download_url)

        # get xpaths for download page
        csv_option = '//*[@id="layout-column-main"]/table/tbody/tr/td[1]/div/section/div/div/div/table/tbody/tr/td/table/tbody/tr/td/table[2]/tbody/tr[13]/td/span/label'
        transaction_dropdown = '//*[@id="transactionDropDown"]'
        continue_button = '//*[@id="id_btn_continue"]'

        # choose download options and click continue
        driver.find_element_by_xpath(csv_option).click()        
        select = Select(driver.find_element_by_xpath(transaction_dropdown))
        select.select_by_value('A')        
        driver.find_element_by_xpath(continue_button).click()