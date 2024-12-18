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
        sleep(1)

        password = self.driver.find_elements(By.CLASS_NAME, 'css-j074to.e2z2zkb0')[1]
        password.clear()
        password.send_keys(local.password)
        sleep(1)

        self.submit()
        sleep(5)

    def submit(self):
        submit = self.driver.find_element(By.CLASS_NAME, "css-h0m9oy.efn4aem0")
        submit.click()
        sleep(5)

    def logout(self):
        exit_btm = self.driver.find_element(By.CLASS_NAME, "css-1oslnw8.efn4aem0")
        exit_btm.click()
        sleep(5)

    def test_authorised(self):
        self.assertEqual(self.driver.find_element(By.LINK_TEXT, "Плиско И.А.").text, "Плиско И.А.")
        self.logout()
        self.assertEqual(self.driver.find_element(By.CLASS_NAME, "css-10rndjo.e1tqmvqp4").text, "Гость")
        self.driver.close()


if __name__ == '__main__':
    unittest.main()