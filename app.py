# -*- coding: utf-8 -*-
# @Time    : 2021/7/30 11:57
# @Author  : ShaoJK
# @File    : app.py
# @Remark  :


from flask import Flask

from views import inventory, purchase
from modules import db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///LiteDB.db'
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True # 自动commit
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
db.init_app(app)

app.register_blueprint(inventory)
app.register_blueprint(purchase)

with app.app_context():
    db.create_all()
@app.route('/')
def hello_world():
    return 'Hello, World!'



if __name__ == '__main__':
    app.run()