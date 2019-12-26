"""
============================
Author:小眼睛.周
Time:2019/11/20
E-mail:245950785@qq.com
============================
"""
import os
import unittest
from library.HTMLTestRunnerNew import HTMLTestRunner
from common.contants import CASE_DIR, REPORT_DIR


# 第一步：创建测试套件
suite = unittest.TestSuite()

# 第二步加载用例到套件
loader = unittest.TestLoader()
suite.addTest(loader.discover(CASE_DIR))


# 第三步：创建一个测试用例运行程序

report_path = os.path.join(REPORT_DIR, "report.html")

with open(report_path, "wb") as f:
    runner = HTMLTestRunner(stream=f,
                            title="接口测试报告",
                            description="接口测试",
                            tester="小眼睛.周"
                            )
    # 第一步：运行测试套件
    runner.run(suite)
