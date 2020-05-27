# -*- encoding: utf-8 -*-
"""
@File    : login_page_locator.py
@Time    : 2020/5/20 11:29
@Author  : xiaobin
@Email   : 343577336@qq.com
@Tel     : 18502888027
@Software: PyCharm
"""

from selenium.webdriver.common.by import By


class LoginPageLocator:
    """登录页面元素定位"""

    # 立即使用按钮
    useNow_button = (By.XPATH, '//button[@class="ant-btn home_box1_button"]')
    # 用户名文本输入框
    user_input = (By.XPATH, '//input[@id="username"]')
    # 密码文本输入框
    pwd_input = (By.XPATH, '//input[@id="password"]')
    # 登录按钮
    login_button = (By.XPATH, '//div[@class="login-box"]//button')
    # 用户名错误、密码错误提示信息
    user_pwd_errorPrompt = (By.XPATH, '//div[contains(@class,"ant-message-custom-content")]//span')
    # 用户名、密码为空提示信息
    user_pwd_empty = (By.XPATH, '//div[@class="ant-form-explain"]')
