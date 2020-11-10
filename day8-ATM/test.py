# Author:xqkang
# Date:2020/10/9 上午11:17
user_data = {
    'account_id': None,
    'is_authenticated': False,
    'account_data': None

}

def update_user_data():
    user_data["is_authenticated"] = True
    print(user_data)

update_user_data()

print(user_data)