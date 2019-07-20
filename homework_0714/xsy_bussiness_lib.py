import time

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from python.homework_0714.xsy_object_ui import LOGIN_LINK, LOGIN_USER, LOGIN_PWD, LOGIN_BTN,\
    CREATE_API,CREATE_API_NAME,SELECT_PORT,CREATE_API_PATH,CREATE_API_SAVEBTN,CREATE_API_BODYRAW,\
    CREATE_API_VALUEASSIGNMENT,CREATE_API_RAWCONTENT,CREATE_API_RAWCONTENT_SAVEBTN,CREATE_API_RUNBTN,CREATE_API_RUN_URL

class UI_uinittest(object):
    # driver = None
    def __init__(self, p_driver):
        self.driver = p_driver
    #登录系统
    def doclever_login(self,p_user,p_pwd):
        self.new_find_element(LOGIN_LINK).click()
        self.new_find_element(LOGIN_USER).clear()
        self.new_find_element(LOGIN_USER).send_keys(p_user)
        self.new_find_element(LOGIN_PWD).clear()
        self.new_find_element(LOGIN_PWD).send_keys(p_pwd)
        self.new_find_element(LOGIN_BTN).click()

    def create_port(self,p_api_name,p_action,p_api_uri,p_para):
        #创建接口
        self.new_find_element(CREATE_API).click()
        time.sleep(1)
        self.new_find_element(CREATE_API_NAME).send_keys(p_api_name)
        self.new_find_element(SELECT_PORT).click()
        time.sleep(1)
        self.driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='" + p_action + "'])").click()
        self.new_find_element(CREATE_API_PATH).send_keys(p_api_uri)
        time.sleep(1)
        if len(p_para)==0:
            self.new_find_element(CREATE_API_SAVEBTN).click()
            time.sleep(2)
        if self.is_element_present(By.ID,"bodyRaw"):
            self.new_find_element(CREATE_API_BODYRAW).click()
            self.new_find_element(CREATE_API_VALUEASSIGNMENT).click()
            self.new_find_element(CREATE_API_RAWCONTENT).clear()
            self.new_find_element(CREATE_API_RAWCONTENT).send_keys(p_para)
            self.new_find_element(CREATE_API_RAWCONTENT_SAVEBTN).click()
            time.sleep(1)
            self.new_find_element(CREATE_API_SAVEBTN).click()
            time.sleep(2)
    def run_api(self,p_url):
        # 运行接口
        self.new_find_element(CREATE_API_RUNBTN).click()
        time.sleep(1)
        self.new_find_element(CREATE_API_RUN_URL).send_keys(p_url)
        time.sleep(1)
        self.new_find_element(CREATE_API_RUNBTN).click()
        time.sleep(5)

    def doclever_logout(self):
        #退出
        ActionChains(self.driver).move_to_element(self.driver.find_element_by_xpath("//*[@id='app']/div[1]/div[2]/div/div[3]/div")).perform()
        time.sleep(5)
        self.driver.find_element_by_xpath("//*[contains(text(),'退出')]").click()


    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True

    def new_find_element(self,p_obj):
        i = p_obj.index('=') #获取=的位置
        if p_obj.startswith('id'):
            return self.driver.find_element_by_id(p_obj[i+1:])
        elif p_obj.startswith('xpath'):
            return self.driver.find_element_by_xpath(p_obj[i+1:])
        elif p_obj.startswith('link text'):
            return self.driver.find_element_by_link_text(p_obj[i+1:])
        elif p_obj.startswith('name'):
            return self.driver.find_element_by_name(p_obj[i+1:])
        elif p_obj.startswith('tag name'):
            return self.driver.find_element_by_class_name(p_obj[i+1:])
        elif p_obj.startswith('css selector'):
            return self.driver.find_element_by_css_selector(p_obj[i+1:])
        elif p_obj.startswith('partial link text'):
            return self.driver.find_element_by_partial_link_text(p_obj[i+1:])
        else:
            return None