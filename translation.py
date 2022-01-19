# -*- codeing = utf-8 -*-
# @time :2022/1/1915:22
# @Author : park
# @File :translation.py
# @Software:PyCharm
import json
import urllib


def translate(content):
    centens = content
    url = "http://fanyi.youdao.com/translate"
    head = {}
    head['user-agent'] ="Mozilla / 5.0(Windows NT 10.0; WOW64) AppleWebKit / 537.36(KHTML,likeGecko) Chrome/87.0.4280.88 Safari/537.36"
    data = {}
    data['i'] = centens
    data['form'] = 'auto'
    data['smartresult'] = 'dict'
    data['client'] = 'fanytideskweb'
    data['salt'] = '1605796372935'
    data['sign'] = '0965172abb459f8c7a791df418bf51c'
    data['lts'] = '1605799637293'
    data['bv'] = 'f7d97c24a497388db1420108e6c3537b'
    data['doctype'] = 'json'
    data['version'] = '2.1'
    data['keyfrom'] = 'fanyi.web'
    data['action'] = 'fy_by_reltlme'
    data = urllib.parse.urlencode(data).encode('utf-8')
    req = urllib.request.Request(url,data,head)
    response = urllib.request.Request(req)
    html = response.read().decode('utf-8')
    req = json.loads(html)
    result = req['translateResult'][0][0]['tgt']
    return result

if __name__ == '__main__':
    print(translate(content="None"))

