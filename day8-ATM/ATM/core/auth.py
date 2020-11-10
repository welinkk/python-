# Author:xqkang
# Date:2020/10/9 下午3:00
import os
from core import db_handler
from conf import settings
from core import logger
import json
import time

def acc_auth(account, password):
    path = db_handler.db_handler(settings.DATABASE)
    account_file = '%s%s.json' % (path, account)
    print(account_file)
    if os.path.isfile(account_file):
        print("--------------")
        with open(account_file, "r") as f:
            account_data = json.load(f)
            if account_data["password"] == password:
                # 将expire_date转化成时间戳
                exp_time_stamp = time.mktime(time.strptime(account_data['expire_date'], "%Y-%m-%d"))
                if time.time() > exp_time_stamp:
                    print("\033[31;1mAccount%s has expired,please contact the back to get a new card!\033[0m" % account)
                else:

                    return account_data
            else:
                print("\033[31;1mAccount ID or password is incorrect!\033[0m")
    else:
        print("\033[31;1mAccount ID does not exist!\033[0m")

def acc_login(user_data, log_obj):
    '''
    account login func
    :user_data: user info data , only saves in memory
    :return:
    '''

    retry_count = 0
    while user_data["is_authenticated"] is not True and retry_count < 3:
        account = input("\033[32;1maccount:\033[0m")
        password = input("\033[32;1mpassword:\033[0m")
        auth = acc_auth(account, password)
        if auth:
            user_data['is_authenticates'] = True
            print("user_data['is_authenticates']:", user_data['is_authenticates'])
            print(user_data)
            user_data['account_id'] = account
            return auth
        retry_count += 1
    else:
        log_obj.error("account too many login attempts")
        exit()

