# -*- coding: utf-8 -*-
# @Time    : 2021/7/30 12:14
# @Author  : ShaoJK
# @File    : api.py
# @Remark  :
import time
from core.Session import Session
from config import TIMEOUT_WAIT_INTERVAL, TIMEOUT_RETRY_NUMBER
from requests.exceptions import ConnectionError
api = Session()

def queryStock(code):
    print("ERP查询库存信息：",code)
    for i in range(TIMEOUT_RETRY_NUMBER):
        try:
            response = api.execute("gy.erp.new.stock.get",{
                "page_no": 1,
                "page_size": 30,
                "item_code": code,
                "cancel": 0
            })
            break
        except ConnectionError as e:
            print("ERP请求超时",e)
            time.sleep(TIMEOUT_WAIT_INTERVAL)
    return response

def queryItem(code):
    print("ERP查询商品信息：",code)
    for i in range(TIMEOUT_RETRY_NUMBER):
        try:
            response = api.execute("gy.erp.items.get",{
                "page_no": 1,
                "page_size": 30,
                "code": code
            })
            break
        except ConnectionError as e:
            print("ERP请求超时",e)
            time.sleep(TIMEOUT_WAIT_INTERVAL)
    return response
