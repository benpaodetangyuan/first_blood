from apps.model.goods import Goods
from flask_restful import Resource, fields, reqparse, marshal
from flask import Blueprint, redirect, url_for, jsonify
from apps.model import db

good_bp = Blueprint('good', __name__)

good_field = {'goods': {
    'name': fields.String,
    'description': fields.String,
    'address': fields.String,
    'price': fields.Float
}}
home_parse = reqparse.RequestParser()
home_parse.add_argument('name', type=str, help='   ', nullable=False, location='form')


class HomeResourse(Resource):
    def get(self):
        goods = Goods.query.filter_by().all()
        goods = marshal(goods, good_field)
        return jsonify(goods)

    def post(self):
        args = home_parse.parse_args()
        name = args.get('name')
        good = Goods.query.filter_by(name=name).first()
        if good is not None:
            db.session.delete(good)
            db.session.commit()
        else:
            return jsonify({'message': 'The name is not exists.'})


good_grounding_field = {"goods": {
    'name': fields.String,
    'description': fields.String,
    'address': fields.String,
    'price': fields.Integer
}}
ground_parse = reqparse.RequestParser()
ground_parse.add_argument('name', type=str, help='商品名称格式错误！', nullable=False, location='form')
ground_parse.add_argument('description', type=str, help='商品描述格式错误！', nullable=False, location='form')
ground_parse.add_argument('address', type=str, help='图片地址格式错误！', nullable=False, location='form')
ground_parse.add_argument('price', type=float, help='商品价格格式错误！', nullable=False, location='form')


class Grounding(Resource):
    def get(self):
        goods = Goods.query.filter_by().all()
        goods = marshal(goods, good_grounding_field)
        return jsonify(goods)

    def post(self):
        args = ground_parse.parse_args()
        name = args.get('name')
        description = args.get('description')
        address = args.get('address')
        price = args.get('price')
        good = Goods(name=name, description=description, address=address, price=price)
        db.session.add(good)
        db.session.commit()
        return redirect(url_for('.home'))


good_undercarriage_field = {"goods": {
    'name': fields.String
}}
undercarriage_parse = reqparse.RequestParser()
undercarriage_parse.add_argument('name', type=str, help='商品名称格式错误！', nullable=False, location='form')


class UnderCarriage(Resource):
    def get(self):
        goods = Goods.query.filter_by().all()
        goods = marshal(goods, good_undercarriage_field)
        return jsonify(goods)

    def post(self):
        args = undercarriage_parse.parse_args()
        name = args.get('name')
        good = Goods.query.filter_by(name=name).first()
        db.session.delete(good)
        db.session.commit()
        return jsonify({'msg': 'succeed'})
