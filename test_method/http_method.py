import requests


class HttpRequests:
    def http_request(self, url, headers, http_method, data=None):
        try:
            if http_method.upper() == 'GET':
                res=requests.get(url, headers=headers)

            elif http_method.upper() == 'POST':
                res=requests.post(url, headers=headers, data=data)

            elif http_method.upper() == 'PATCH':
                 res = requests.patch(url, headers=headers, data=data)

            else:
                print("可能是方法错了")
        except Exception as e:
            print("请求报错了：{0}".format(e))
            raise e
        return res


if __name__ == '__main__':
    from test_method .get_token_method import Request

    token=(Request().get_token())
    get_url="http://106.15.172.195/user-api/user/v1/tokens"
    data='{"email":"cjc123456@163.com","password":"123456"}'
    headers={"Content-Type": "application/json"}
    res=HttpRequests().http_request(get_url, headers, "POST")
    print(res.text)
