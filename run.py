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

pytest.main(['--html=HtmlTestReport/report.html', '--junitxml=HtmlTestReport/report.xml'])
