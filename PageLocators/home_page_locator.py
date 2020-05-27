# -*- encoding: utf-8 -*-
"""
@File    : home_page_locator.py
@Time    : 2020/5/22 11:15
@Author  : xiaobin
@Email   : 343577336@qq.com
@Tel     : 18502888027
@Software: PyCharm
"""

from selenium.webdriver.common.by import By


class HomePageLocator:
    """首页元素定位"""

    # 用户昵称
    nick_name = (By.XPATH, '//div[@class="name"]')
    # 查询文本输入框
    search_input = (By.XPATH, '//input[@placeholder="search"]')
    # 查询按钮
    search_button = (By.XPATH, '//*[name()="svg" and @data-icon="search"]')
    # 清除查询条件按钮
    clear_search_button = (By.XPATH, '//*[name()="svg" and @data-icon="close-circle"]')
    # 导出按钮
    export_button = (By.XPATH, '//span[@class="down"]/i')
    # 物料PartNo
    partNo_materials = (By.XPATH, '//span[@class="part-number"]')
    # 物料总数量
    total_qty_materials = (By.XPATH, '//td[4]//div')
    # 物料在库数量
    inStock_num_materials = (By.XPATH, '//td[5]//div')
    # 物料在途数量
    inTransit_num_materials = (By.XPATH, '//td[6]//div')
    # 物料在产数量
    inProduction_num_materials = (By.XPATH, '//td[7]//div')
    # 物料列表记录总条数
    total_num_list_materials = (By.XPATH, '//div[@class="pagination-total"]')
    # 查询数据为空的提示信息文本
    search_empty_prompt = (By.XPATH, '//p[@class="ant-empty-description"]')
