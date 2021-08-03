# -*- coding: utf-8 -*-
# @Time    : 2021/7/30 12:00
# @Author  : ShaoJK
# @File    : inventory.py
# @Remark  :
from flask import Blueprint

from api import api, queryItem, queryStock
from core.utils import wrap_response, get_params, get_post_form
from modules import Item

inventory = Blueprint('inventory',__name__,url_prefix="/inventory")

@inventory.route('/query')
def getInventory():
    page = get_params('page',1)
    pageSize = get_params('pageSize',10)
    itemCode = get_params('itemCode')
    cancel = get_params('cancel', 'false') == 'true'
    response = api.execute("gy.erp.new.stock.get",{
        "page_no": int(page),
        "page_size": int(pageSize),
        "item_code": itemCode,
        "cancel": int(cancel)
    })
    return wrap_response(response)


@inventory.route('/queryBatch', methods=['POST'])
def getInventoryByBatch():
    itemList = get_post_form().itemList
    inventory = dict([(item,None) for item in itemList])
    content = []
    for item in inventory.keys():
        res = Item.getItem(item)
        inventory[item] = {'supplier_outerid':res['supplier_outerid']}
    for item in inventory.keys():
        response = queryStock(item)
        inventory[item].update(dict([(stock['sku_code'],stock) for stock in response['stocks']]))
    return wrap_response(inventory)

@inventory.route('/allItems')
def allItems():
    return wrap_response([item.toJson() for item in Item.query.all()])