# -*- encoding: utf-8 -*-
"""
@File    : pro_path.py
@Time    : 2020/5/19 16:26
@Author  : xiaobin
@Email   : 343577336@qq.com
@Tel     : 18502888027
@Software: PyCharm
"""

import os

# 项目顶级目录
project_path = os.path.split(os.path.split(os.path.realpath(__file__))[0])[0]
# 测试数据目录
test_data_path = os.path.join(project_path, 'TestData', 'test_data.yaml')
# 公共配置文件目录
common_data_path = os.path.join(project_path, 'Config', 'common_conf.yaml')
# 日志文件目录
log_path = os.path.join(project_path, 'Log')
# 截图文件路径
screen_shot_path = os.path.join(project_path, 'ScreenShot')


