# Author:xqkang
# Date:2020/10/9 下午1:42
import json
import time
from core import db_handler
from conf import settings

def load_current_balance(account_id):

    '''
    return account balance and other basic info
    :param account_id:
    :return:
    '''

    db_path = db_handler.db_handler(settings.DATABASE)

    account_file = "%s/%s.json" % (db_path, account_id)
    with open(account_file, "r") as f:
        acc_data = json.load(f)
        return acc_data

def print_acc():
    print(load_current_balance("1234"))

def dump_accounts(account_data):
    '''
    after updated transaction or account data , dump it back to file db
    :param account_data:
    :return:
    '''
    db_path = db_handler.db_handler(settings.DATABASE)
    account_file = "%s/%s.json" % (db_path, account_data["id"])
    with open(account_file, "w") as f:
        print(">>>>>>>>>>>>>", account_data)
        json.dump(account_data, f)
        return True

