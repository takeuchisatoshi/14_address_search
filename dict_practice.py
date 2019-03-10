address_data = [{"address1": "岩手県",
                 "address2": "八幡平市",
                 "address3": "大更",
                 "zipcode": "0287111"},

                {"address1": "兵庫県",
                 "address2": "西宮市",
                 "address3": "高須町",
                 "zipcode": "6638141"},
                ]

if __name__ == '__main__':
    print(f"{address_data[1]['address1']}{address_data[1]['address2']}{address_data[1]['address3']}\n")
    print(f"{address_data[0]['address1']}{address_data[0]['address2']}{address_data[0]['address3']}\n")

    # 別パターン
    address1 = address_data[1]['address1']
    address2 = address_data[1]['address2']
    address3 = address_data[1]['address3']
    print(f"{address1}{address2}{address3}\n")

    address1 = address_data[1]['address1']
    address2 = address_data[0]['address2']
    address3 = address_data[0]['address3']
    print(f"{address1}{address2}{address3}")
