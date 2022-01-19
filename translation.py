import urllib.request
import urllib.parse
import json


def translate(content):
    centens = content
    url = 'http://fanyi.youdao.com/translate'
    head = {}
    head['user-agent'] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36 Edg/96.0.1054.62"
    data = {}
    data['i'] = centens
    data['from'] = 'auto'
    data['to'] = 'auto'
    data['smartresult'] = 'dict'
    data['client'] = 'fanyideskweb'
    data['salt'] = '16057996372935'
    data['sign'] = '0965172abb459f8c7a791df4184bf51c'
    data['lts'] = '1605799637293'
    data['bv'] = 'f7d97c24a497388db1420108e6c3537b'
    data['doctype'] = 'json'
    data['version'] = '2.1'
    data['keyfrom'] = 'fanyi.web'
    data['action'] = 'fy_by_realtlme'
    data = urllib.parse.urlencode(data).encode('utf-8')
    req = urllib.request.Request(url, data, head)
    response = urllib.request.urlopen(req)
    html = response.read().decode('utf-8')
    req = json.loads(html)
    result = req['translateResult'][0][0]['tgt']
    return result


if __name__ == '__main__':
    print(translate(content="None"))

