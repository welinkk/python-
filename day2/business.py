# Author:xqkang
# Date:2020/9/20 下午1:40
import json
''''
products = [
    ["iphone  12", 4500],
    ["huawei p40", 6000],
    ["bike  6300", 2000]
]
'''
json_path = "products.json"

def put_product_w(json_path, list):
    list_json = json.dumps(list)
    products_obj = open(json_path, "w")
    products_obj.write(list_json)
    products_obj.close()


def get_product(json_path):
    products_obj = open(json_path, "rb")
    products_read = products_obj.read()
    products = json.loads(products_read)
    products_obj.close()
    return list(products)

def put_product_a(json_path,list):
    list_json = json.dumps(list)
    products_obj = open(json_path, "a")
    products_obj.write(list_json)
    products_obj.close()


def update_read_product(json_path, index, price):
    with open(json_path, "rb") as f:
        params = json.load(f)
        params[index-1][1] = price
        print("params:", params)
        products = params

    with open(json_path, "w") as f:
        params = json.dumps(products)
        f.write(params)
        f.close()

#put_product_w(json_path, products)
#update_read_product(json_path, 1, 99999)
def change_product_price():
    while True:
        print("-------------修改价格-------------")
        product_list = get_product(json_path)
        for index, i in enumerate(product_list):
            print(index+1, i)
        chang_id = int(input("输入想修改的编号："))
        chang_price = input("输入想修改的价格：")
        update_read_product(json_path, chang_id, chang_price)
        print("The \033[321m{0}\033[0m price had bean change!!! ".format(product_list[chang_id-1][0]))

        print("修改后的价格列表:")
        product_list = get_product(json_path)
        for index, i in enumerate(product_list):
            print(index+1, i)

        enter_quit = input("是否想要退出？按\"q\"退出，\"enter\"继续")
        if enter_quit == "q":
            print("正在退出系统......")
            break

    print("\n")
    print("\n")

def add_product():
    while True:
        print("---------------添加商品---------------")
        product_list = get_product(json_path)
        print("当前商品列表：")
        for index, i in enumerate(product_list):
            print(index + 1, i)
        print("\n")

        product_name = input("输入你想添加的商品名称：")
        product_price = input("输入你想添加的商品的价格：")
        print("数组名称类型：", type(product_list[0][0]))
        print("数组价格类型：", type(product_list[0][1]))
        print("输入的名称类型：", type(product_name))
        print("输入的价格类型：", type(product_price))
        product_list.append([product_name][product_price])
        print(product_list)




add_product()
