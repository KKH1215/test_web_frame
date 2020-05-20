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

# 日志文件目录
log_path = os.path.join(project_path, 'Log')


if __name__ == '__main__':
    print(project_path)
    print(log_path)
