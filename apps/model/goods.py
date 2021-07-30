from . import db


class Goods(db.Model):
    __tablename__ = 'goods'
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(255))
    description = db.Column(db.Text)
    address = db.Column(db.String(255))
    price = db.Column(db.FLOAT())

    def __init__(self, name, description, address, price):
        self.name = name
        self.description = description
        self.address = address
        self.price = price
