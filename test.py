# Author:xqkang
# Date:2020/9/15 下午5:08
true_age = 23
print(type(true_age))
count = 0
while True:
    if count == 3:
        print("You guess three times,logout...")
        break
    guess_age = input("guess a age:")
    if type(true_age) == str:
        print("we need a number!!!")
        continue
    else:
        guess_age = int(guess_age)
    if guess_age == true_age:
        print("You got it!!!")
    elif guess_age > true_age:
        print("You guess a little bigger!!! ")
    else:
        print("You guess a little smaller !!! ")
    count += 1