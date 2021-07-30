# -*- coding: utf-8 -*-
# @Time    : 2021/7/30 9:35
# @Author  : ShaoJK
# @File    : Session.py
# @Remark  : 连接管易云ERP session类
import hashlib
import hmac
import json
import random
import re
import time
from urllib.parse import urlparse, urlunparse

import requests
from requests import Session

from config import ERP_SECRET, ERP_APPKEY, ERP_SESSIONKEY, ERP_URL

absolute_http_url_regexp = re.compile(r"^https?://", re.I)

# urllib3.disable_warnings(urllib3.exceptions.SecurityWarning)  # 关闭urllib的警告提示

class Session(Session):
    def _build_url(self, path):
        """ prepend url with hostname unless it's already an absolute URL """
        if absolute_http_url_regexp.match(path):
            return path
        else:
            if "/api/" in path:
                return "%s%s" % (self.base_url.split("?")[0], path)
            return "%s%s" % (self.base_url.split("?")[0], path)

    def sign(self, data: str):
        if type(data) != str:
            data = json.dumps(data)
        data = ERP_SECRET + data + ERP_SECRET
        md5 = hashlib.md5()
        md5.update(data.encode('utf-8'))
        sign = md5.hexdigest().upper()
        return sign

    def execute(self, method,body):
        print(body)
        body["appkey"] = ERP_APPKEY
        body["sessionkey"] = ERP_SESSIONKEY
        body["method"] = method
        body["sign"] = self.sign(json.dumps(body).replace(": ",":").replace(", ",","))
        return self.post(ERP_URL, data=json.dumps(body).encode('utf-8')).json()
