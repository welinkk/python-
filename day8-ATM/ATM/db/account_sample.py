# Author:xqkang
# Date:2020/10/9 上午10:09

import json
acc_dic = {
    'id': 1234,
    'password': 'abc',
    'credit': 15000,
    'balance': 15000,
    'enroll_date': '2020-01-02',
    'expire_date': '2025-01-01',
    'pay_day': 22,
    'status': 0 # 0 = normal, 1 = locked, 2 = disabled
}
print(json.dump(acc_dic))
