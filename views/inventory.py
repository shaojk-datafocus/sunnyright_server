# -*- coding: utf-8 -*-
# @Time    : 2021/7/30 12:00
# @Author  : ShaoJK
# @File    : inventory.py
# @Remark  :
from flask import Blueprint

from api import api
from core.utils import wrap_response, get_params

inventory = Blueprint('inventory',__name__,url_prefix="/inventory")

@inventory.route('/query')
def getInventory():
    page = get_params('page',1)
    pageSize = get_params('pageSize',10)
    itemCode = get_params('itemCode')
    cancel = get_params('cancel', 'false') == 'true'
    print(type(cancel))
    print(bool(cancel))
    print(int(bool(cancel)))
    response = api.execute("gy.erp.new.stock.get",{
        "page_no": int(page),
        "page_size": int(pageSize),
        "item_code": itemCode,
        "cancel": int(bool(cancel))
    })
    return wrap_response(response)
