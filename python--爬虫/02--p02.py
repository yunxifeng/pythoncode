from urllib import request, error

if __name__ == "__main__":
    url = "http://www.renren.com/969284066/profile"
    headers = {
        "Cookie":"anonymid=jq9g68uudji33n; depovince=HEN; _r01_=1; JSESSIONID=abcBHEibTkFU79tuk95Fw; ick_login=e52a5a50-8938-40f2-84d2-c32832372438; t=725054d6a540a96fcdf4c7f9c76685eb6; societyguester=725054d6a540a96fcdf4c7f9c76685eb6; id=969284066; xnsid=5f09c64; jebecookies=25bc2c04-9278-491e-a4a1-b9135817d6a6|||||; ver=7.0; loginfrom=null; wp_fold=0"
    }

    req = request.Request(url, headers=headers)
    rep = request.urlopen(req)
    html = rep.read().decode()

    with open("rsp2.html", "w", encoding="utf-8") as f:
        f.write(html)
