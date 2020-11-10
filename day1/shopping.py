# Author:xqkang
# Date:2020/9/18 下午5:34



products = [[1, "iphone_12", 4500],[2, "huaweip40", 6000],[3, "bike_6300", 2000]]
choices = []

print("###########################################")
print("########### Happy Shopping ################")
print("###########################################")
# 获取消费者金钱总数
consumer_money = int(input("How manny money do you have?money:"))
balance = consumer_money
while True:
    print("-------------------------------------------")


    print(" What product do you want to buy?(Chose the number)")

    #列出商品
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("~~~~~~~~~~~~~~ product list ~~~~~~~~~~~~~~~")
    for i in products:
        print(i)
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

    choice = int(input("My choice is:"))-1

    product_money = int(products[choice][2])
    print(product_money)
    if balance > product_money:

        balance = balance - product_money
        choices.append(products[choice])

        print("You have choice：")
        for j in choices:
            print(j)
        print("your balance is:", balance)
        print("do you want to quit? y or n")
        confirm = input("")
        if confirm == "y":
            break
    else:
        print("you didn't have enough money")
        break


print("You have buy:")
for k in choices:
    print(k)
print("Your balance is:", balance)
