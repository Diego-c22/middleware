"""Resources to connect to Carrito model"""
from flask import Blueprint
from db.db import DataBase
from flask_restful import Resource, Api, abort, reqparse

cart_v1 = Blueprint("cart_v1", __name__)
api = Api(cart_v1)


class CartResource(Resource):
    def get(self):
        db = DataBase()
        response = db.select_all("Carritos")
        return response, 200

    def post(self):
        args = arguments.parse_args()
        db = DataBase()
        response = db.insert_element("Carritos", "IdCarrito", **args)
        return response, 200


arguments = reqparse.RequestParser()
arguments.add_argument('IdUsuario', type=int,
                       help="Este campo es obligatorio", required=True)
arguments.add_argument(
    'IdArticulo', type=int, help="Este campo es obligatorio", required=True)
arguments.add_argument(
    'Cantidad', type=int, help="Este campo es obligatorio", required=True)
arguments.add_argument('IdUsuario', type=int,
                       help="Este campo es obligatorio", required=True)


api.add_resource(CartResource, "/middleware/tienda/carritos/")


class CartResourceDetail(Resource):
    def get(self, id):
        db = DataBase()
        response = db.select_detail("Carritos", "IdCarrito", id)
        return response, 200

    def patch(self, id):
        args = arguments_update.parse_args()
        db = DataBase()
        response = db.update_element("Carritos", "IdCarrito", id, **args)
        return response, 200

    def delete(self, id):
        db = DataBase()
        response = db.delete_element("Carritos", "IdCarrito", id)
        return response, 200


arguments_update = reqparse.RequestParser()
arguments_update.add_argument('IdUsuario', type=int,
                              help="Este campo es obligatorio", required=False)
arguments_update.add_argument(
    'IdArticulo', type=int, help="Este campo es obligatorio", required=False)
arguments_update.add_argument(
    'Cantidad', type=int, help="Este campo es obligatorio", required=False)
arguments_update.add_argument('IdUsuario', type=int,
                              help="Este campo es obligatorio", required=False)


api.add_resource(CartResourceDetail, "/middleware/tienda/carritos/<int:id>/")
