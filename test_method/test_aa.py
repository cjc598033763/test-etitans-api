from test_method.get_token_method import Request
from test_method import lianxixi
from test_method.get_token_method import Request
import requests

lianxixi.headers["Authorization"]=Request().get_token()
def res_():
    res = requests.put(lianxixi.url, data=lianxixi.body1, headers=lianxixi.headers)
    return res.text


if  __name__=='__main__':
    print(res_())