# Author:xqkang
# Date:2020/9/19 下午7:43

data = {
    "北京": {
        "昌平": {
            "沙河": ["ooo", "ssss"],
            "天通苑": ["ooo", "ssss"]},
        "海淀": {
            "沙河": ["ooo", "ssss"],
            "aa": ["ooo", "ssss"]},
        },
    "山东": {
        "德州": {},
        "青岛": {},
        "济南": {}
    }
}
exit_flag = False
while not exit_flag:
    for i in data:
        print(i)
    choice = input("选择进入一级目录>>:")
    if choice in data:
        while not exit_flag:
            for j in data[choice]:
                print(j)
            choice2 = input("选择进入二级目录>>:")
            if choice2 in data[choice]:
                while not exit_flag:
                    for k in data[choice][choice2]:
                        print(k)
                    choice3 = input("选择进入三级目录>>:")
                    if choice3 in data[choice][choice2]:
                        for l in data[choice][choice2][choice3]:
                            print(l)
                        choice4 = input("最后一层按b返回：")
                        if choice4 == "b":
                            pass
                        elif choice4 == "q":
                            exit_flag = True
                    if choice3 == "b":
                        break
                    elif choice3 == "q":
                        exit_flag = True
            if choice2 == "b":
                break
            elif choice2 == "q":
                exit_flag = True