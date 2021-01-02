import requests
import logging

class Request_api():
    def http_post(self, url, param, header=None):
        res = requests.post(url=url, data=param, headers=header, timeout = 10)
        return res
    def http_get(self, url, param, header=None):
        res = requests.get(url=url, params=param, headers=header)
        return res
    def http_request(self, method, url, param, header=None):
        if method in ['get','GET']:
            res = self.http_get(url, param, header)
            return res
        elif method in ['post','POST']:
            res = self.http_post(url, param, header)
            return res
        else:
            return '请求方法错误！'
if __name__ == '__main__':
    http = Request_api()
    method = 'post'
    url = 'http://47.114.130.18:8080/cms/manage/loginJump.do'
    param = {
        'userAccount':'admin',
        'loginPwd':'1234567'
    }
    header = {}
    res = http.http_request(method,url,param,header)
    print(res.json())