# -*- encoding: utf-8 -*-
"""
@File    : run.py
@Time    : 2020/5/25 11:50
@Author  : xiaobin
@Email   : 343577336@qq.com
@Tel     : 18502888027
@Software: PyCharm
"""

import pytest

#  自动收集、运行用例，自动生成测试报告。失败用例自动重新运行一次
pytest.main(
    ['--reruns', '1', '--reruns-delay', '5', '--html=HtmlTestReport/report.html',
     '--junitxml=HtmlTestReport/report.xml'])
