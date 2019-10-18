from xlrd import open_workbook
from xlutils.copy import copy
from openpyxl import load_workbook
from test_Util.read_config import ReadConfig
from test_Util import project_path
from test_method.get_token_method import Request
import io
import sys

sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='gb18030')  # 改变标准输出的默认编码


class DoExcel:
    def __init__(self, file_name):
        self.file_name = file_name
        self.rb = open_workbook(self.file_name)
        self.mode = eval(ReadConfig.get_config(project_path.test_config_path, 'MODE', 'mode'))

    def excel_sheet_nrows(self):
        """返回excel的行数"""
        return self.sheet.nrows - 1

    def read_header(self):
        for key in self.mode:
            self.sheet = self.rb.sheet_by_name(key)


    def update_header(self):
        """更新header请求参数"""
        for key in self.mode:
            wb = copy(self.rb)
            self.sheet = self.rb.sheet_by_name(key)
            for j in range(1, self.sheet.nrows):
                if 'Authorization' in self.sheet.cell_value(j, 2):
                    token = Request().get_token()
                    update_token=eval(self.sheet.cell_value(j, 2))["Authorization"]=token
                    update_token_dict=eval(self.sheet.cell_value(j, 2))
                    update_token_dict["Authorization"]=update_token
                    ws = wb.get_sheet(key)
                    ws.write(j, 2, str(update_token_dict))
                    wb.save(self.file_name)

                else:
                    continue

            # ws = wb.get_sheet(key)

            # for i in range(1, self.sheet.nrows):
            #     token = Request().get_token()
            #     ws.write(i, 2, str({"Authorization": token}))
            #     wb.save(self.file_name)

    def get_data(self):
        """获得data数据"""
        self.update_header()
        test_data = []
        for key in self.mode:

            self.sheet = self.rb.sheet_by_name(key)
            if self.mode[key] == 'all':
                for i in range(1, self.sheet.nrows):  # 循环第二行中所有行数据
                    row_data = {}
                    row_data['case'] = self.sheet.cell_value(i, 0)  # 拿到case的值
                    row_data['url'] = self.sheet.cell_value(i, 1)  # 循环第i行，的第1列
                    row_data['headers'] = eval(self.sheet.cell_value(i, 2))  # 循环第i行，的第2列
                    row_data['method'] = self.sheet.cell_value(i, 3)  # 拿到method的值
                    row_data['data'] = self.sheet.cell_value(i, 4).encode('utf-8')
                    row_data['title'] = self.sheet.cell_value(i, 5)
                    row_data['except'] = self.sheet.cell_value(i, 6)
                    row_data['sheet_name'] = key
                    test_data.append(row_data)
            else:
                for case_id in self.mode[key]:
                    row_data = {}
                    row_data['case'] = self.sheet.cell_value(case_id, 0)  # 拿到case的值

                    row_data['url'] = self.sheet.cell_value(case_id, 1)  # 循环第i行，的第1列
                    row_data['headers'] = eval(self.sheet.cell_value(case_id, 2))  # 循环第i行，的第2列

                    row_data['method'] = self.sheet.cell_value(case_id, 3)  # 拿到method的值
                    row_data['data'] = self.sheet.cell_value(case_id, 4).encode('utf-8')

                    row_data['title'] = self.sheet.cell_value(case_id, 5)
                    row_data['except'] = self.sheet.cell_value(case_id, 6)
                    row_data['sheet_name'] = key
                    test_data.append(row_data)
        return test_data

    def write_back(self, i, sheet_name, result, test_result):
        wb = copy(self.rb)
        ws = wb.get_sheet(sheet_name)
        ws.write(i, 7, result)
        ws.write(i, 8, test_result)
        wb.save(self.file_name)


if __name__ == '__main__':
    print((DoExcel(r'data01.xls').get_data()))
