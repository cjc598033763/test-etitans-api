from test_method.get_token_method import Request
import requests
url="http://dev-api.cb08af099262a4f2797e7b24914168322.cn-shanghai.alicontainer.com/inquiries"
headers={"Content-Type": "application/json", "token":Request().get_token() }
data='{"contact_name":"abcccc"}'
r= requests.patch(url, headers=headers,data=data)
print(r.text)