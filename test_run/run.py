import unittest
import os
import HTMLTestRunnerCN
from test_Util.project_path import test_report_path
from testcase.test_case import test_login

project_path=(os.path.split(os.path.split(os.path.realpath(__file__))[0])[0])
test_case_path=os.path.join(project_path,'testcase')
discover = unittest.defaultTestLoader.discover(test_case_path, 'test*.py')


# test_case = unittest.TestSuite()
# discover = unittest.defaultTestLoader.discover(test_case_path,pattern="test_case.py",top_level_dir=None)
with open(test_report_path,"wb")as file:
    runner=HTMLTestRunnerCN.HTMLTestRunner(stream=file, verbosity=2, title="測試報告", description="這是單元測試報告")  # 收集報告並生成報告
    runner.run(discover)