# -*- encoding: utf-8 -*-
"""
@File    : test_materials_list.py
@Time    : 2020/5/24 22:47
@Author  : xiaobin
@Email   : 343577336@qq.com
@Tel     : 18502888027
@Software: PyCharm
"""

import time
import pytest
from Common.my_logger import log
from Common.read_yaml import test_data
from PageObjects.home_page import HomePage


@pytest.mark.usefixtures('login_web')
class TestSearchMaterialsList:

    @pytest.mark.smoke
    @pytest.mark.parametrize('data', test_data['search_success'])
    def test_search_success(self, login_web, data):
        log.info('===========物料列表页查询用例：正常场景：使用正确的partNO=========')
        # 登录步骤 ：输入物料号，点击查询按钮，   比对数据：当前页物料号对比，总条数对比
        home_page = HomePage(login_web)
        home_page.search(data['partNo'])
        time.sleep(5)  # 因为查询操作后，引起了页面的变化，所以加了强制等待
        if len(data['expect']) > 1:
            try:
                for item in home_page.get_all_part_no_materials():
                    assert data['expect'][0] in item
                assert data['expect'][1] == home_page.get_total_num_list_materials()
            except AssertionError:
                log.exception('断言失败，用例不通过！')
                raise
        else:
            try:
                assert data['expect'][0] == home_page.get_total_num_list_materials()
            except AssertionError:
                log.exception('断言失败，用例不通过！')
                raise

    @pytest.mark.parametrize('data', test_data['search_fail'])
    def test_search_fail(self, login_web, data):
        login_web.implicitly_wait(10)
        log.info('===========物料列表页查询用例：异常场景：料号不存在、输入特殊字符、汉字=========')
        home_page = HomePage(login_web)
        home_page.search(data['partNo'])
        time.sleep(2)
        try:
            assert home_page.get_list_materials_empty_msg() == data['expect']
        except AssertionError:
            log.exception('断言失败，用例不通过！')
            raise

    def test_clear_search_button(self):
        pass

    def test_export_button(self):
        pass
