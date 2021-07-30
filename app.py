# -*- coding: utf-8 -*-
# @Time    : 2021/7/30 11:57
# @Author  : ShaoJK
# @File    : app.py
# @Remark  :


from flask import Flask

from views import inventory, purchase

app = Flask(__name__)
app.register_blueprint(inventory)
app.register_blueprint(purchase)
@app.route('/')
def hello_world():
    return 'Hello, World!'



if __name__ == '__main__':
    app.run()