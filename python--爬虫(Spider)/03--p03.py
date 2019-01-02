'''
版本二
处理js加密代码
'''
'''
通过查找,获取js中的加密算法
1.计算salt的公式: i = "" + (new Date).getTime() + parseInt(10 * Math.random(), 10);
2.sign: n.md5("fanyideskweb" + e + i + "p09@Bn{h02_BIEe]$P^nG")
3.md5一共需要四个参数,第一个和第四个固定,第三个是salt,通过代码确定第二个参数就是输入的要查找的单词
'''
import time,random

def getSalt():
    '''
    计算salt: i = "" + (new Date).getTime() + parseInt(10 * Math.random(), 10);
    转换为python代码
    (new Date).getTime(): 得到时间戳
    parseInt(10 * Math.random(): 生成0-10的随机数
    :return:
    '''
    salt = int(time.time()*1000) + random.randint(0,10)
    return salt

# 求sign
def getMD5(v):
    import hashlib
    md5 = hashlib.md5()
    # update需要一个bytes格式的参数
    md5.update(v.encode("utf-8"))
    sign = md5.hexdigest()
    return sign
def getSign(key,salt):
    sign = "fanyideskweb" + key + str(salt) + "p09@Bn{h02_BIEe]$P^nG"
    sign = getMD5(sign)
    return sign


from urllib import request,parse

def youdao(key):
    url = "http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule"
    salt = getSalt()
    data = {
        "i": key,
        "from": "AUTO",
        "to": "AUTO",
        "smartresult": "dict",
        "client": "fanyideskweb",
        # 加盐(很长的随机字串)
        "salt": str(salt),
        # 数字签名
        "sign": str(getSign(key,salt)),
        "ts": "1546145159512",
        "bv": "37074a7035f34bfbf10d32bb8587564a",
        "doctype": "json",
        "version": "2.1",
        "keyfrom": "fanyi.web",
        "action": "FY_BY_REALTIME",
        "typoResult": "false"
    }
    print(data)
    data = parse.urlencode(data).encode("utf-8")
    headers = {
        "Accept":"application/json,text/javascript,*/*;q = 0.01",
        #"Accept-Encoding":"gzip,deflate",
        "Accept-Language":"zh-CN,zh;q=0.9",
        "Connection":"keep-alive",
        "Content-Length":str(len(data)),
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
    youdao("girl")
