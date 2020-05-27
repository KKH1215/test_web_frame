# -*- encoding: utf-8 -*-
"""
@File    : read_yaml.py
@Time    : 2020/5/20 10:04
@Author  : xiaobin
@Email   : 343577336@qq.com
@Tel     : 18502888027
@Software: PyCharm
"""

from ruamel.yaml import YAML
from Common.my_logger import log
from Common.pro_path import *


class ReadYaml:

    @staticmethod
    def read_yaml(filepath):
        """
        读取yaml文件内容
        :param filepath: 文件路径
        :return:
        """
        if os.path.exists(filepath):
            load_yaml = YAML(typ='safe')
            with open(filepath, encoding='utf-8') as file:
                try:
                    return load_yaml.load(file)
                except Exception as e:
                    log.error('读取配置文件报错，请检查你的yaml文件填写是否正确！')
                    raise e
        else:
            log.error('配置文件不存在！')
            raise FileNotFoundError


# 实例化对象
yaml = ReadYaml()
# 读取url地址和登录账号
common_data = yaml.read_yaml(common_data_path)
# 读取测试数据
test_data = yaml.read_yaml(test_data_path)


