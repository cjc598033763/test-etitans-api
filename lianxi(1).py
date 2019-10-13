import requests

url="http://106.15.172.195/user-api/user/v1/tokens"
header={"Content-Type":"application/json; charset=utf-8"}
data={"email":"cjc123456@163.com","password":"123456"}

res=requests.post(url,header,data)
print(res.text)