from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest
from time import sleep
import local


class TestWebSelenium(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://eios.kemsu.ru/a/eios")
        self.driver.maximize_window()
        sleep(5)

        login = self.driver.find_elements(By.CLASS_NAME, 'css-j074to.e2z2zkb0')[0]
        login.clear()
        login.send_keys("stud71735")

        password = self.driver.find_elements(By.CLASS_NAME, 'css-j074to.e2z2zkb0')[1]
        password.clear()
        password.send_keys(local.password)

        self.submit()



    def submit(self):
        submit = self.driver.find_element(By.CLASS_NAME, "css-h0m9oy.efn4aem0")
        submit.click()
        sleep(5)

    def logout(self):
        exit_btm = self.driver.find_element(By.CLASS_NAME, "css-1oslnw8.efn4aem0")
        exit_btm.click()
        self.driver.close()

    def test_authorised(self):
        self.assertEqual(self.driver.find_element(By.LINK_TEXT, "Плиско И.А.").text, "Плиско И.А.")
        self.logout()


if __name__ == '__main__':
    unittest.main()