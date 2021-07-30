# -*- coding: utf-8 -*-
# @Time    : 2021/7/30 11:21
# @Author  : ShaoJK
# @File    : test.py
# @Remark  :
from core.Session import Session

client = Session()
response = client.api("gy.erp.purchase.get", {
    "page_no": "1",
    "page_size": "10",
    "status": "0"})
print(response.text)