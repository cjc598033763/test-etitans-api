from test_method.get_token_method import Request
import requests
import json


url="http://dev-api.cb08af099262a4f2797e7b24914168322.cn-shanghai.alicontainer.com/user-api/app/v1/inquiries"
headers={"Content-Type": "application/json", "Authorization": Request().get_token()}
data='{"pickup_date":"2019-10-30","shipper":{"location":{"country":"US","zipcode":"98409","region_l1":" WA","region_l2":" TACOMA","name":"","name2":"","address":""},"contact":{"name":"","phone":"","phone_ext":"","email":""}},"consignee":{"location":{"country":"US","zipcode":"91744","region_l1":" CA","region_l2":" CITY OF INDUSTRY","name":"","name2":"","address":""},"contact":{"name":"","phone":"","phone_ext":"","email":""}},"commodities":[{"name":"book","weight":"1","length":"1","width":"1","height":"1","package_type":"PKG","count":1,"hazardous":false,"description":"book"}],"shipment_specifics":{"cube_unit":"m³","weight_unit":"Kg","length_unit":"m"},"options":{"pickup":[{"code":"Local-PayOnBehalf"}],"delivery":[],"other":[]}}'.encode("utf-8")
r=requests.post(url, headers=headers, data=data)
print(r.text)
# requests =  Request("2019-10-30", "98409")
# dumps=json.dumps(requests)

