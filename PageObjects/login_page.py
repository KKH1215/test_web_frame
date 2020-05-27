# -*- encoding: utf-8 -*-
"""
@File    : login_page.py
@Time    : 2020/5/21 10:42
@Author  : xiaobin
@Email   : 343577336@qq.com
@Tel     : 18502888027
@Software: PyCharm
"""

from Common.base_page import BasePage
from PageLocators.login_page_locator import LoginPageLocator


class LoginPage(LoginPageLocator, BasePage):

    # 登录功能
    def login(self, username, pwd):
        name = '登录页面_登录功能'
        self.wait_ele_visible(self.useNow_button, model=name)
        self.click_ele(self.useNow_button, model=name)
        self.wait_ele_visible(self.user_input, model=name)
        self.input_text(self.user_input, username, model=name)
        self.input_text(self.pwd_input, pwd, model=name)
        self.click_ele(self.login_button, model=name)

        # try:
        #     WebDriverWait(self.driver, 10, 0.5).until(EC.visibility_of_element_located(self.useNow_button))
        #     self.driver.find_element(*self.useNow_button).click()
        #     WebDriverWait(self.driver, 10, 0.5).until(EC.visibility_of_element_located(self.user_input))
        #     self.driver.find_element(*self.user_input).send_keys(username)
        #     self.driver.find_element(*self.pwd_input).send_keys(pwd)
        #     WebDriverWait(self.driver, 10, 0.5).until(EC.visibility_of_element_located(self.user_input))
        #     self.driver.find_element(*self.login_button).click()
        # except Exception:
        #     raise

    # 获取用户名、密码错误提示信息
    def get_error_msg_login(self):
        name = '登录页面_错误用户和密码提示信息'
        self.wait_ele_visible(self.user_pwd_errorPrompt, model=name)
        return self.get_text(self.user_pwd_errorPrompt, model=name)

    # 获取用户名或密码为空提示信息
    def get_empty_msg_login(self):
        name = '登录页面_用户名或密码为空提示信息'
        self.wait_ele_visible(self.user_pwd_empty, model=name)
        return self.get_text(self.user_pwd_empty, model=name)

    # 获取用户名和密码都为空提示信息
    def get_all_empty_msg_login(self):
        name = '登录页面_用户名和密码为空提示信息'
        self.wait_ele_visible(self.user_pwd_empty, model=name)
        return self.get_all_text(self.user_pwd_empty, model=name)
