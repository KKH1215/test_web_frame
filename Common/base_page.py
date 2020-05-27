# -*- encoding: utf-8 -*-
"""
@File    : base_page.py
@Time    : 2020/5/26 21:20
@Author  : xiaobin
@Email   : 343577336@qq.com
@Tel     : 18502888027
@Software: PyCharm
"""

import os
import time
import win32gui
import win32con
from Common.my_logger import log
from Common.pro_path import screen_shot_path
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver


class BasePage:

    def __init__(self, driver: WebDriver):
        self.driver = driver

    # 等待元素可见方法
    def wait_ele_visible(self, locator, wait_time=15, poll_frequency=0.5, model=''):
        """

        :param locator: 类型为元组(By.XXX,定位表达式)
        :param wait_time: 等待时间
        :param poll_frequency: 轮询周期，就是每隔0.5s就查看一次
        :param model: 模块名称
        """
        log.info('等待元素可见。')
        try:
            WebDriverWait(self.driver, wait_time, poll_frequency).until(EC.visibility_of_element_located(locator))
            log.info('{0}模块: 元素 {1}已可见'.format(model, locator))
        except Exception:
            # 失败的时候，捕获异常到日志中。并且截图
            log.exception('等待元素可见失败')
            self._screen_shot(model)
            raise

    # 等待元素存在
    def wait_ele_present(self, locator, wait_time=20, poll_frequency=0.5, model=''):
        log.info('等待元素存在')
        try:
            WebDriverWait(self.driver, wait_time, poll_frequency).until(EC.presence_of_element_located(locator))
            log.info('{0}模块: 元素 {1}已可见'.format(model, locator))
        except Exception:
            log.exception('等待元素存在失败')
            self._screen_shot(model)
            raise

    # 查找元素
    def find_ele(self, locator, model=''):
        log.info('{0}：开始查找元素：{1}'.format(model, locator))
        try:
            return self.driver.find_element(*locator)
        except Exception:
            log.exception('查找元素失败')
            self._screen_shot(model)
            raise

    # 查找多个元素
    def find_all_ele(self, locator, model=''):
        log.info('{0}：开始查找符合表达式的所有元素：{1}'.format(model, locator))
        try:
            return self.driver.find_elements(*locator)
        except Exception:
            log.exception('查找多个元素失败')
            self._screen_shot(model)
            raise

    # 输入操作
    def input_text(self, locator, text, model=''):
        # 查找元素
        ele = self.find_ele(locator, model)
        log.info('{0}：元素：{1} 输入内容：{2}'.format(model, locator, text))
        try:
            ele.send_keys(text)
        except Exception:
            log.exception('输入操作失败了')
            self._screen_shot(model)
            raise

    # 点击操作
    def click_ele(self, locator, model=''):
        ele = self.find_ele(locator, model)
        log.info('{0}：元素：{1} 点击操作'.format(model, locator))
        try:
            ele.click()
        except Exception:
            log.exception('点击操作失败了')
            self._screen_shot(model)
            raise

    # 获取元素的文本
    def get_text(self, locator, model=''):
        # 找到元素
        ele = self.find_ele(locator, model)
        log.info('{0}：获取元素：{1}的文本内容'.format(model, locator))
        try:
            log.info('{0}：获取元素：{1}的文本内容是：{2}'.format(model, locator, ele.text))
            return ele.text
        except Exception:
            log.exception('获取元素文本失败')
            self._screen_shot(model)
            raise

    # 获取多个元素的文本内容,并返回列表
    def get_all_text(self, locator, model=''):
        ele = self.find_all_ele(locator, model)
        log.info('{0}：获取多个元素：{1}的文本内容'.format(model, locator))
        try:
            text_list = []
            for item in ele:
                text_list.append(item.text)
            log.info('{0}：获取多个元素：{1}的文本内容是：{2}'.format(model, locator, text_list))
            return text_list
        except Exception:
            log.exception('获取多个元素文本失败')
            self._screen_shot(model)
            raise

    # 获取元素属性值
    def get_ele_attribute(self, locator, attribute_name, model=''):
        ele = self.find_ele(locator, model)
        log.info('{0}：元素：{1}的属性：{2}'.format(model, locator, attribute_name))
        try:
            value = ele.get_attribute(attribute_name)
            log.info('{0}：元素：{1}的属性：{2} 值是：{3}'.format(model, locator, attribute_name, value))
            return value
        except Exception:
            log.exception('获取元素属性值失败')
            self._screen_shot(model)
            raise

    # 上传操作
    def upload(self, filepath, model=''):
        log.info('执行上传操作')
        try:
            dialog = win32gui.FindWindow("#32770", "打开")  # 一级窗口
            # 找到窗口
            com_box32 = win32gui.FindWindowEx(dialog, 0, "ComboBoxEx32", None)  # 二级窗口
            com_box = win32gui.FindWindowEx(com_box32, 0, "comboBox", None)  # 三级窗口
            edit = win32gui.FindWindowEx(com_box, 0, "Edit", None)  # 四级
            button = win32gui.FindWindowEx(dialog, 0, "button", None)  # 四级---打开按钮
            # 操作
            win32gui.SendMessage(edit, win32con.WM_SETTEXT, None, filepath)  # 发送文件路径
            win32gui.SendMessage(dialog, win32con.WM_COMMAND, 1, button)  # 点击打开按钮
        except Exception:
            log.exception('上传文件操作失败')
            self._screen_shot(model)
            raise

    # 截图
    def _screen_shot(self, model_name):
        now = time.strftime('%Y-%m-%d %H_%M_%S', time.localtime())
        filepath = screen_shot_path + '/{0}_{1}.png'.format(model_name, now)
        self.driver.save_screenshot(filepath)
        log.info('截图成功，图片名称：{}'.format(os.path.split(filepath)[1]))

    # 提交表单操作
    def submit_form(self):
        pass

    # 执行js语句操作
    def js_execute(self):
        pass
        # self.driver.execute_script()

    # 鼠标悬浮操作
    def action_chains_perform(self):
        pass

    # 键盘操作



