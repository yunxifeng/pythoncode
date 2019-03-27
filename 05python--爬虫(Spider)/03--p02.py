'''
版本一
破解有道翻译
'''
from urllib import request,parse

def youdao(danci):
    url = "http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule"
    data = {
        "i": "girl",
        "from": "AUTO",
        "to": "AUTO",
        "smartresult": "dict",
        "client": "fanyideskweb",
        # 加盐(很长的随机字串)
        "salt": "15461451595129",
        # 数字签名
        "sign": "4948dd297de898ebf0d0353d50c36252",
        "ts": "1546145159512",
        "bv": "37074a7035f34bfbf10d32bb8587564a",
        "doctype": "json",
        "version": "2.1",
        "keyfrom": "fanyi.web",
        "action": "FY_BY_REALTIME",
        "typoResult": "false"
    }
    data = parse.urlencode(data).encode("utf-8")
    headers = {
        "Accept":"application/json,text/javascript,*/*;q = 0.01",
        #"Accept-Encoding":"gzip,deflate",
        "Accept-Language":"zh-CN,zh;q=0.9",
        "Connection":"keep-alive",
        "Content-Length":"254",
        "Content-Type":"application/x-www-form-urlencoded;charset=UTF-8",
        "Cookie":"OUTFOX_SEARCH_USER_ID=-1272854714@10.169.0.82;JSESSIONID=aaagM5ZKBZVGsaZ_PB9Fw;OUTFOX_SEARCH_USER_ID_NCOO=424891421.8256569;___rl__test__cookies=1546145159500",
        "Host":"fanyi.youdao.com",
        "Origin":"http://fanyi.youdao.com",
        "Referer":"http://fanyi.youdao.com",
        "User-Agent":"Mozilla/5.0(Windows NT 10.0; WOW64) AppleWebKit/537.36(KHTML, like Gecko) Chrome/69.0.3497.100Safari/537.36",
        "X-Requested-With":"XMLHttpRequest"
    }
    req = request.Request(url=url, headers=headers, data=data)
    rsp = request.urlopen(req)
    html = rsp.read().decode()
    print(html)
if __name__ == "__main__":
    youdao("boy")
