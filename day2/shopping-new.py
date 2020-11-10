# Author:xqkang
# Date:2020/9/18 下午5:34
import json

products = [
    ("iphone  12", 4500),
    ("huawei p40", 6000),
    ("bike  6300", 2000)
]

print("###########################################")
print("~~~~~~~~~~~~~ Happy Shopping ~~~~~~~~~~~~~~")
print("###########################################")
# 获取消费者金钱总数
consumer_money = None
choices = []
while True:
    try:
        consumer_money = int(input("How manny money do you have?money:"))
        break
    except Exception:
        print("you should give me a \033[33;1mdigit\033[0m!!!")
        continue

balance = consumer_money

while True:
    print("-------------------------------------------")

    print(" What product do you want to buy?(Choice the number or print \"q\" to quit )")

    # 列出商品
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("-------------- \033[32;1mproduct list\033[0m ---------------")
    for index, i in enumerate(products):
        print(index+1, i)
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

    #choice = int(input("My choice is:")) - 1
    choice = input("My choice is:")
    if choice.isdigit():
        choice = int(choice)
        if choice <= len(products) and choice > 0:

            product_price = int(products[choice-1][1])

            if balance > product_price:
                balance = balance - product_price
                choices.append(products[choice-1])

                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                print("------------- \033[32;1mSelected list\033[0m ---------------")
                for index, j in enumerate(choices):
                    print(index+1, j)
                print("your balance is:\033[31;1m%s\033[0m" %(balance))

            else:
                print("you didn't have enough money")
                break
        else:
            print("\033[31;1m please give me a right number!!!\033[0m")
    elif choice == "q":
        print("you have quited.....")
        break
    else:
        continue

print("You have buy:")
for index, k in enumerate(choices):
    print(index+1, k)
print("Your balance is:\033[31;1m%s\033[0m" %(balance))
