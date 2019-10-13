import os
project_path=os.path.split(os.path.split(os.path.realpath(__file__))[0])[0]  # 文件根目錄
test_case_path=os.path.join(project_path,'test_Util','data01.xls')  # 用例的路徑
test_report_path=os.path.join(project_path,'test_run','test_api.html')
test_config_path=os.path.join(project_path,'test_Util','case.config')  # 配置文件的路径


path=os.path.realpath(__file__)
