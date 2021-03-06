# -*- encoding: utf-8 -*-
"""
@File    : my_logger.py
@Time    : 2020/5/19 14:05
@Author  : xiaobin
@Email   : 343577336@qq.com
@Tel     : 18502888027
@Software: PyCharm
"""

import time
import logging
from Common.pro_path import log_path


class MyLogger:

    def __init__(self):
        # 创建一个logger容器
        self.logger = logging.Logger('my_log')
        self.logger.setLevel(logging.DEBUG)
        # 创建输出渠道
        now = time.strftime('%Y-%m-%d %H_%M_%S', time.localtime())
        self.fh = logging.FileHandler(log_path + '/{}_web.log'.format(now), encoding='utf-8')
        self.sh = logging.StreamHandler()
        self.fh.setLevel(logging.INFO)
        self.sh.setLevel(logging.INFO)
        # 定义输出格式
        formatter = logging.Formatter('【%(asctime)s】【%(levelname)s】【%(filename)s】'
                                      '【%(funcName)s】【日志信息】：%(message)s', '%Y-%m-%d_%H:%M:%S')
        self.fh.setFormatter(formatter)
        self.sh.setFormatter(formatter)
        # 和logger做对接
        self.logger.addHandler(self.fh)
        self.logger.addHandler(self.sh)
        self.fh.close()
        self.sh.close()


log = MyLogger().logger


