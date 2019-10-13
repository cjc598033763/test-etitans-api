from test_method.http_method import HttpRequests
from test_method import lianxixi


class Request(object):
    def get_token(self):
        url = "http://dev-api.cb08af099262a4f2797e7b24914168322.cn-shanghai.alicontainer.com/user-api/user/v1/tokens"
        if "new_password" in lianxixi.body1:
            a = (eval(lianxixi.body1)["new_password"])
            data = {"email": "cjc598033763@163.com", "password": a}
            header = {"Content-Type": "application/json"}
            res = HttpRequests().http_request(url, header, "POST", data=str(data))
            try:
                return res.json()["content"]["access_token"]
            except TypeError as e:
                print("未获取到token{num}".format(num=e))
                raise e


if __name__ == '__main__':
    print(Request().get_token())
