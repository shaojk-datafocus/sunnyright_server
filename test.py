# # -*- coding: utf-8 -*-
# # @Time    : 2021/7/30 11:21
# # @Author  : ShaoJK
# # @File    : test.py
# # @Remark  :
from core.Session import Session

client = Session()
response = client.execute("gy.erp.items.get", {
    "page_no": "1",
    "page_size": "10",
    "code": "35663"})
print(response)