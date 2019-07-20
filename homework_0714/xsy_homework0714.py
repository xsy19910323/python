# -*- coding: utf-8 -*-

from selenium import webdriver

from selenium.webdriver.common.by import By

import unittest, time

from python.homework_0714.xsy_bussiness_lib import UI_uinittest


class UntitledCase(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.driver = webdriver.Firefox()

    @classmethod
    def tearDownClass(self):
        self.driver.quit()

    def setUp(self):
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.katalon.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
        self.login = UI_uinittest(self.driver)

    def test_1_login(self):
        self.driver.get("http://www.doclever.cn/controller/index/index.html")
        self.login.doclever_login("xsy","967928")
        self.assertTrue(self.login.is_element_present(By.ID, "tab-interface"))
        time.sleep(5)

    def test_2_create_port(self):
        self.driver.find_element_by_xpath("//*[@id='pane-interface']/div/tempalte/div[2]/div[1]/div[2]/div/div/div/table/tbody/tr/td[1]/div/div[1]").click()
        time.sleep(5)
        self.login.create_port("login","POST","/user/login","name=xsy&password=967928")
        self.login.run_api("http://www.doclever.cn:8090")
        self.assertTrue(self.login.is_element_present(By.XPATH, './/*[contains(text(),\'"code":200\')]'))
        time.sleep(3)

    def test_3_logout(self):
        self.login.doclever_logout()
        time.sleep(5)
        self.assertTrue(self.login.is_element_present(By.LINK_TEXT, "登录"))


    def tearDown(self):
        self.assertEqual([], self.verificationErrors)



if __name__ == "__main__":
    unittest.main()
