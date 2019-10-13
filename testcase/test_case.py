import requests
import unittest
from test_method.http_method import HttpRequests
from test_Util.doexcel import DoExcel
from ddt import ddt, data
from test_Util.project_path import test_case_path, test_report_path

test_data = (DoExcel(test_case_path).get_data())


@ddt
class test_login(unittest.TestCase):
    def setUp(self):
        print("开始测试")

    @data(*test_data)
    def test01(self, item):
        """测试结果"""
        res = HttpRequests().http_request(url=item["url"], headers=item["headers"], http_method=item['method'],data=item['data'])
        try:
            self.assertEqual(item["except"], "成功")
            Test_Result = "pass"
        except AssertionError as e:
            Test_Result = "false"
            print("执行用例失败{0}".format(e))
            raise e
        finally:  # 不管错还是对，都会执行
            DoExcel(test_case_path).write_back(item['case'],item['sheet_name'], str(res.json()), Test_Result)  # 結果寫入excel表
            print("获取的结果是：{0}".format(res.json()))

    def tearDown(self):
        print("\n测试结果")


if __name__ == '__main__':
    unittest.main()
