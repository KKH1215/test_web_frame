# -*- encoding: utf-8 -*-
"""
@File    : conftest.py
@Time    : 2020/5/25 10:00
@Author  : xiaobin
@Email   : 343577336@qq.com
@Tel     : 18502888027
@Software: PyCharm
"""

import pytest
from selenium import webdriver
from Common.read_yaml import common_data
from Common.my_logger import log
from PageObjects.login_page import LoginPage


# 登录用例的前置和后置
@pytest.fixture
def init_login():
    log.info('=====用例前置：初始化浏览器会话:打开谷歌浏览器，访问系统网址：{0}======='.format(common_data['web_url']))
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(common_data['web_url'])
    login_page = LoginPage(driver)
    yield [driver, login_page]
    log.info('=====用例后置：关闭谷歌浏览器会话=======')
    driver.quit()


# 登录系统前置和后置
@pytest.fixture
def login_web():
    log.info("=====用例前置：初始化浏览器会话，登录物料可视化系统=======")
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(common_data['web_url'])
    LoginPage(driver).login(common_data['user'], common_data['pwd'])
    yield driver
    log.info('=====用例后置：关闭浏览器会话，关闭浏览器=======')
    driver.quit()
