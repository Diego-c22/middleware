"""Resources to connect to articuloscomprados model"""
from flask import Blueprint
from db.db import DataBase
from flask_restful import Resource, Api, reqparse

solditems_v1 = Blueprint("solditems_v1", __name__)
api = Api(solditems_v1)


class SoldItemsResource(Resource):
    def get(self):
        db = DataBase()
        response = db.select_all("Articuloscomprados")
        return response, 200

    def post(self):
        args = arguments.parse_args()
        db = DataBase()
        response = db.insert_element(
            "Articuloscomprados", "IdArticuloComprado", ** args)
        return response, 200


arguments = reqparse.RequestParser()
arguments.add_argument('IdCompra', type=int,
                       help="Este campo es obligatorio", required=True)
arguments.add_argument(
    'IdArticulo', type=int, help="Este campo es obligatorio", required=True)
arguments.add_argument(
    'Cantidad', type=int, help="Este campo es obligatorio", required=True)


api.add_resource(SoldItemsResource, "/middleware/tienda/articulos_comprados/")


class SoldItemsResourceDetail(Resource):
    def get(self, id):
        db = DataBase()
        response = db.select_detail(
            "Articuloscomprados", "IdArticuloComprado", id)
        return response, 200

    def patch(self, id):
        args = arguments_update.parse_args()
        db = DataBase()
        response = db.update_element(
            "Articuloscomprados", "IdArticuloComprado", id, **args)
        return response, 200

    def delete(self, id):
        db = DataBase()
        response = db.delete_element(
            "Articuloscomprados", "IdArticuloComprado", id)
        return response, 200


arguments_update = reqparse.RequestParser()
arguments_update.add_argument('IdCompra', type=int,
                              help="Este campo es obligatorio", required=False)
arguments_update.add_argument(
    'IdArticulo', type=int, help="Este campo es obligatorio", required=False)
arguments_update.add_argument(
    'Cantidad', type=int, help="Este campo es obligatorio", required=False)


api.add_resource(SoldItemsResourceDetail,
                 "/middleware/tienda/articulos_comprados/<int:id>/")
