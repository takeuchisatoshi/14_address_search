import requests

if __name__ == '__main__':
    url = "http://zipcloud.ibsnet.co.jp/api/search?zipcode=0287111"

    r = requests.get(url)

    print(r.json())
