# Author:xqkang
# Date:2020/10/9 上午9:44
import os
import sys
import logging
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# 数据库
DATABASE = {
    'engine': 'file_stotage',
    'name': 'accounts',
    'path': '%s/db' % base_dir
}

# 日志
LOG_LEVEL = logging.INFO
LOG_TYPES = {
    'transaction': 'transactions.log',
    'access': 'access.log'
}

# 功能
TRANSACTION_TYPE = {
    'repay': {'action': 'plus', 'interest': 0}, # 还款
    'withdraw': {'action': 'minus', 'interest': 0.05}, # 取款
    'transfer': {'action': 'minus', 'interest': 0.05}, # 转账
    'consume': {'action': 'minus', 'interest': 0} # 账单
}