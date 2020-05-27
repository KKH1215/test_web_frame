# -*- encoding: utf-8 -*-
"""
@File    : home_page.py
@Time    : 2020/5/22 22:27
@Author  : xiaobin
@Email   : 343577336@qq.com
@Tel     : 18502888027
@Software: PyCharm
"""

from Common.base_page import BasePage
from PageLocators.home_page_locator import HomePageLocator


class HomePage(HomePageLocator, BasePage):

    # 获取用户昵称
    def get_nick_name(self):
        name = '首页_获取用户昵称'
        self.wait_ele_visible(self.nick_name, model=name)
        return self.get_text(self.nick_name, model=name)

    # 查询功能
    def search(self, part_no):
        name = '首页_查询功能'
        self.wait_ele_visible(self.search_input, model=name)
        self.input_text(self.search_input, part_no, model=name)
        self.click_ele(self.search_button, model=name)

    # 查看物料详情功能
    def see_materials_detail(self):
        name = '首页_查看物料详情功能'
        self.wait_ele_visible(self.partNo_materials, model=name)
        self.click_ele(self.partNo_materials, model=name)

    # 获取当前页PartNo列表数据
    def get_all_part_no_materials(self):
        name = '首页_获取当前页所有物料的PartNo'
        self.wait_ele_visible(self.partNo_materials, model=name)
        return self.get_all_text(self.partNo_materials, model=name)

    # 获取查询列表为空的提示信息
    def get_list_materials_empty_msg(self):
        name = '首页_获取查询列表为空的提示信息'
        self.wait_ele_visible(self.search_empty_prompt, model=name)
        return self.get_text(self.search_empty_prompt, model=name)

    # 获取物料列表总条数功能
    def get_total_num_list_materials(self):
        name = '首页_获取查询列表总条数'
        num = self.get_text(self.total_num_list_materials, model=name)  # "Total Number of Materials：523"
        return int(num.split('：')[1])

    # 获取物料总数量功能
    def get_total_qty_materials(self):
        name = '首页_获取单条记录的物料总数量'
        num = self.get_text(self.total_qty_materials, model=name)  # 6,300,000
        return int(num.replace(',', ''))

    # 获取物料在库数量功能
    def get_in_stock_num_materials(self):
        name = '首页_获取单条记录的物料在库数量'
        num = self.get_text(self.inStock_num_materials, model=name)  # 300,000
        return int(num.replace(',', ''))

    # 获取物料在途数量功能
    def get_in_transit_num_materials(self):
        name = '首页_获取单条记录的物料在途数量'
        num = self.get_text(self.inTransit_num_materials, model=name)  # 300,000
        return int(num.replace(',', ''))

    # 获取物料在产数量功能
    def get_in_production_num_materials(self):
        name = '首页_获取单条记录的物料在产数量'
        num = self.get_text(self.inProduction_num_materials, model=name)  # 300,000
        return int(num.replace(',', ''))
