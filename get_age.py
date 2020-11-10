# Author:xqkang
# Date:2020/9/15 下午3:48

true_age = 23
count = 0
# while count<3:
#     guess_age = int(input("guess a age:"))
#     if guess_age == true_age:
#         print("You got it!!!")
#         break
#     elif guess_age > true_age:
#         print("You guess a little bigger!!! ")
#     else:
#         print("You guess a little smaller !!! ")
#     count +=1
# else:
#     print("You have tried too many times.. fuck off")

# for i in range(3):
#     guess_age = int(input("guess a age:"))
#     if guess_age == true_age:
#         print("You got it!!!")
#         break
#     elif guess_age > true_age:
#         print("You guess a little bigger!!! ")
#     else:
#         print("You guess a little smaller !!! ")
#     count +=1
# else:
#     print("You have tried too many times.. fuck off")

# while count<3:
#     guess_age = int(input("guess a age:"))
#     if guess_age == true_age:
#         print("You got it!!!")
#         break
#     elif guess_age > true_age:
#         print("You guess a little bigger!!! ")
#     else:
#         print("You guess a little smaller !!! ")
#     count +=1
#     if count == 3:
#         count_confirm=input("do you want to continue...?")
#         if count_confirm != 'n':
#             print("1111")
#             count =0

for i in range(0,10):
    if i<3:
        print("loop",i)
    else:
        continue
    print("hehehe....")