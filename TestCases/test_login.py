# -*- encoding: utf-8 -*-
"""
@File    : test_login.py
@Time    : 2020/5/24 22:46
@Author  : xiaobin
@Email   : 343577336@qq.com
@Tel     : 18502888027
@Software: PyCharm
"""

import pytest
from Common.read_yaml import test_data
from Common.my_logger import log
from PageObjects.home_page import HomePage


@pytest.mark.usefixtures('init_login')
class TestLogin:

    # init_login(fixture函数名称)接收 fixture运行的返回值  [driver,login_page]
    @pytest.mark.smoke
    @pytest.mark.parametrize('data', test_data['login_success'])
    def test_login_success(self, init_login, data):
        log.info('===========登陆用例：正常场景：使用正确的用户名和密码登陆=========')
        # 登录步骤 ：输入用户名和密码，点击登录，比对数据：首页昵称
        init_login[1].login(data['user'], data['pwd'])
        try:
            assert HomePage(init_login[0]).get_nick_name() == data['expect']
        except AssertionError:
            log.exception('断言失败，用例不通过！')
            raise

    @pytest.mark.parametrize('data', test_data['login_error_userPwd'])
    def test_login_error_user_pwd(self, init_login, data):
        log.info('===========登陆用例：异常场景：使用错误的用户名和密码登陆=========')
        # 登录步骤 ：输入用户名和密码，点击登录，比对数据：您输入的用户名或密码不正确
        init_login[1].login(data['user'], data['pwd'])
        try:
            assert init_login[1].get_error_msg_login() == data['expect']
        except AssertionError:
            log.exception('断言失败，用例不通过！')
            raise

    @pytest.mark.parametrize('data', test_data['login_empty_userPwd'])
    def test_login_empty_user_pwd(self, init_login, data):
        log.info('===========登陆用例：异常场景：用户名或密码为空=========')
        # 登录步骤 ：输入用户名和密码，点击登录，比对数据：请输入用户名或邮箱, 请输入密码
        init_login[1].login(data['user'], data['pwd'])
        try:
            assert init_login[1].get_empty_msg_login() == data['expect']
        except AssertionError:
            log.exception('断言失败，用例不通过！')
            raise

    @pytest.mark.parametrize('data', test_data['login_all_empty_userPwd'])
    def test_login_all_empty_user_pwd(self, init_login, data):
        log.info('===========登陆用例：异常场景：用户名和密码为空=========')
        # 登录步骤 ：输入用户名和密码，点击登录，比对数据：['请输入用户名或邮箱', '请输入密码']
        init_login[1].login(data['user'], data['pwd'])
        try:
            assert init_login[1].get_all_empty_msg_login() == data['expect']
        except AssertionError:
            log.exception('断言失败，用例不通过！')
            raise
