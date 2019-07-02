import requests
import lxml.html
import time

etree = lxml.html.etree

def get_img(url,headers):
    res = requests.get(url=url,headers=headers).text
    res = etree.HTML(res)
    img_list = res.xpath("//img/@data-lazyload")[:20]

    print(img_list)
    for i in img_list:
        print(i[-3:])
        if(i[-3:] == "jpg"):

            r = requests.get(url=i,headers=headers).content
            print("G:\\untitled6\\crawler\\img\\zaocan\\"+i[-8:])

            with open(i[-1:-8],"wb") as f:
                f.write(r)
            time.sleep(1)

if __name__ == "__main__":
    url = "http://www.dianping.com/shop/98546557"
    headers = {
        "Host": "www.dianping.com",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36",
    }
    get_img(url,headers)