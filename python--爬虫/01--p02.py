# 利用urllib.request下载页面
# 自动检测页面编码
from urllib import request
import chardet
if __name__ == "__main__":
    url = "http://www16.zzu.edu.cn/msgs/vmsgisapi.dll/onemsg?msgid=1812181411208224074&ds8=88648054"
    rsp = request.urlopen(url)
    html = rsp.read()
    # 利用chardet自动检测
    cs = chardet.detect(html)
    # cs类型: dict
    print(type(cs))
    # {'encoding': 'UTF-8-SIG', 'confidence': 1.0, 'language': ''}
    print(cs)

    # 使用get取值,如果chardet检测到了,就用获取到的"encoding",如果检测不到,则使用"utf-8"
    # 保证不会报错
    html = html.decode(cs.get("encoding", "utf-8"))
    print(html)