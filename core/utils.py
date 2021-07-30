# -*- coding: utf-8 -*-
# @Time    : 2021/7/30 10:02
# @Author  : ShaoJK
# @File    : utils.py
# @Remark  : 通用工具
import json
import time

from flask import request


class Dict(dict):
    """用属性的形式使用字典"""

    def __getattr__(self, key):
        if key not in self.keys():
            return None
        return self.get(key)

    def __setattr__(self, key, value):
        self[key] = value

    def forUpdate(self,*args):
        """返回更新数据的字典，去除对象中的id
            *args: 为属性值，存在则仅返回所给的更新项
        """
        if len(args)>0:
            return dict([(key,None if self[key]=='' else self[key]) for key in args])
        else:
            return dict([(key,value) for key,value in self.items() if key!='id'])

def toDict(l:list,key=None)->Dict:
    """传列表，返回字典，key:需要做关键字的属性项,不填则是数字"""
    d = Dict()
    if key:
        for item in l:
            d[item[key]] = item
    else:
        for i,item in enumerate(l):
            d[i] = item
    return d

def wrap_response(data=None,errCode=0, exception="",**kwargs):
    """包装返回的json格式，确保全站统一
        可是输入额外的键值对，改键值对讲附加在response信息中
    """
    return json.dumps({"data": data, "errCode": errCode, "exception": exception, "success": errCode==0, **kwargs})

def get_post_form() -> Dict:
    """获取POST表单"""
    req = request.data.decode('utf-8')
    if req:
        return Dict(json.loads(req))
    return Dict()

def get_params(key: str,default=None):
    """获取GET参数"""
    value = request.args.get(key)
    if value: return value
    return default

def get_current_time() -> str:
    return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

def timestamp_to_str(t) -> str:
    return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(t))

def str_to_timestamp(s,pattern="%Y-%m-%d %H:%M:%S") -> float:
    return time.strptime(s, pattern)
