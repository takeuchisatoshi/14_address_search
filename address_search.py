import requests

if __name__ == '__main__':
    url = "http://zipcloud.ibsnet.co.jp/api/search?zipcode=0287111"
    r = requests.get(url)
    address_dict = r.json()
    # print(r.json())

    address1 = address_dict["results"][0]["address1"]
    address2 = address_dict["results"][0]["address2"]
    address3 = address_dict["results"][0]["address3"]

    print(f"{address1}{address2}{address3}")
