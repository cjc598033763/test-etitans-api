# lt=['"00501"\n','"00611"\n']
# f= open("regions.txt","r")
# line=f.readlines()
# a=str(line).replace("\\n","").replace("'","")
# print(a)

# a=["11","22"]
# print(type(a.index("22")))

# !/usr/bin/python
# -*- coding: <gbk> -*-
import xlrd
import requests
from xlutils.copy import copy
import time
def get_token():
    url="http://106.15.172.195/user-api/user/v1/tokens"
    headers={"Content-Type":"application/json"}
    data={"email": "cjc598033763@163.com", "password": "c1234567"}
    res=requests.post(url=url,json= data,headers=headers)
    try:
        res_token=res.json()["content"]["access_token"]
    except TypeError as e:
        print("出現問題：{0}".format(e))
        raise e
    return res_token

b=get_token()
data=xlrd.open_workbook("abc.xls")
data_=copy(data)
ws=data_.get_sheet(0)
table=data.sheets()[0]
for i in range(0, table.nrows):
    site={"header": "我"}
    a={"Authorization":b}
    ws.write(i, 1, label=str(a))
data_.save('abc.xls')
data1=xlrd.open_workbook("abc.xls")
table1=data1.sheets()[0]
print("---------------------------------------"+str(table1.nrows))
headers_=table1.cell(0,1).value
headerss_=(eval(headers_))
list_=[]
for i in range(0,table1.nrows):
    a=table1.cell(i,1).value
    list_.append(a)

#
for item in list_:
    user_url="http://106.15.172.195/user-api/user/v1/self/info"
    res_=requests.get(url=user_url,headers=eval(item))
    print(res_.text)



