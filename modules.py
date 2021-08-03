from flask_sqlalchemy import SQLAlchemy

from api import api, queryItem

db = SQLAlchemy()

class Item(db.Model):
    __tablename__ = 'item'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    code = db.Column(db.String(32))
    name = db.Column(db.String(256))
    cancel = db.Column(db.Boolean)
    supplier_code = db.Column(db.String(32))
    supplier_outerid = db.Column(db.String(32))
    pic_url = db.Column(db.String)

    def __getitem__(self, item):
        return getattr(self, item)

    def keys(self):
        return ('id', 'code', 'name', 'cancel', 'supplier_code', 'supplier_outerid', 'pic_url')

    def toJson(self):
        return dict(self)

    @staticmethod
    def getItem(code):
        item = Item.query.filter_by(code=code).first()
        if item is None:
            res = queryItem(code)['items'][0]
            item = Item(code=res['code'],name=res['name'],cancel=res['del'],pic_url=res['pic_url'],
                supplier_code=res['supplier_code'],supplier_outerid=res['supplier_outerid'])
            db.session.add(item)
            db.session.flush()
        return item

    