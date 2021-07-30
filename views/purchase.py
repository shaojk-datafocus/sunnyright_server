# -*- coding: utf-8 -*-
# @Time    : 2021/7/30 14:30
# @Author  : ShaoJK
# @File    : purchase.py
# @Remark  : 

from flask import Blueprint

from api import api
from core.utils import wrap_response, get_params

purchase = Blueprint('purchase',__name__,url_prefix="/purchase")

@purchase.route('/query')
def getPurchase():
    page = get_params('page',1)
    pageSize = get_params('pageSize',10)
    code = get_params('code')
    startCreateDate = get_params('startCreateDate')
    endCreateDate = get_params('endCreateDate')
    startApproveDate = get_params('startApproveDate')
    endApproveDate = get_params('endApproveDate')
    status = get_params('status', 'false') == 'true'
    response = api.execute("gy.erp.purchase.get",{
        "page_no": int(page),
        "page_size": int(pageSize),
        "code": code,
        "start_create_date": startCreateDate,
        "end_create_date": endCreateDate,
        "start_approve_date": startApproveDate,
        "end_approve_date": endApproveDate,
        "status": status
    })
    return wrap_response(response)
