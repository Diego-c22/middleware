"""Resources to connect with Compras model"""
from flask import Blueprint
from db.db import DataBase
from flask_restful import Resource, Api, abort, reqparse

purchase_v1 = Blueprint("purchase_v1", __name__)
api = Api(purchase_v1)


class PurchaseResource(Resource):
    def get(self):
        try:
            db = DataBase()
            response = db.select_all("Compras")
            print(response)
            return response, 200
        except Exception as e:
            raise e
            abort(404, message="No se encontraron elementos")

    def post(self):
        args = arguments.parse_args()
        db = DataBase()
        response = db.insert_element("Compras", **args)
        print(response)
        return response, 200


arguments = reqparse.RequestParser()
arguments.add_argument('PrecioTotal', type=float,
                       help="Este campo es obligatorio", required=True)
arguments.add_argument(
    'FechaCompra', type=str, help="Este campo es obligatorio", required=True)
arguments.add_argument(
    'RastreoCompras', type=int, help="Este campo es obligatorio", required=True)
arguments.add_argument('IdUsuario', type=int,
                       help="Este campo es obligatorio", required=True)


api.add_resource(PurchaseResource, "/middleware/tienda/compras/")


class PurchaseResourceDetail(Resource):
    def get(self, id):
        db = DataBase()
        response = db.select_detail("Compras", "IdCompra", id)
        return response, 200

    def patch(self, id):
        args = arguments_update.parse_args()
        db = DataBase()
        response = db.update_element("Compras", "IdCompra", id, **args)
        return response, 200

    def delete(self, id):
        db = DataBase()
        response = db.delete_element("Compras", "IdCompra", id)
        return response, 200


arguments_update = reqparse.RequestParser()
arguments_update.add_argument('PrecioTotal', type=float,
                              help="Este campo es obligatorio", required=False)
arguments_update.add_argument(
    'FechaCompra', type=str, help="Este campo es obligatorio", required=False)
arguments_update.add_argument(
    'RastreoCompras', type=int, help="Este campo es obligatorio", required=False)
arguments_update.add_argument('IdUsuario', type=int,
                              help="Este campo es obligatorio", required=False)


api.add_resource(PurchaseResourceDetail, "/middleware/tienda/compras/<int:id>")
