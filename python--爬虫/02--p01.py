from urllib import request, error

if __name__ == "__main__":
    url = "http://www.renren.com/969284066/profile"
    rsp = request.urlopen(url)
    html = rsp.read().decode()
    with open("rsp1.html", "w", encoding="utf-8") as f:
        f.write(html)
