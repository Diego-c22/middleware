"""Resources to connect to Articulos model"""
from flask import Blueprint
from db.db import DataBase
from flask_restful import Resource, Api, abort, reqparse

items_v1 = Blueprint("items_v1", __name__)
api = Api(items_v1)


class ItemResource(Resource):
    def get(self):
        db = DataBase()
        response = db.select_all("Articulos")
        print(response)
        return response, 200

    def post(self):
        args = arguments.parse_args()
        db = DataBase()
        response = db.insert_element("Articulos", "IdArticulo", ** args)
        return response, 200


arguments = reqparse.RequestParser()
arguments.add_argument('IdCategoriadearticulo', type=int,
                       help="Este campo es obligatorio", required=True)
arguments.add_argument(
    'Nombre', type=str, help="Este campo es obligatorio", required=True)
arguments.add_argument(
    'Marca', type=str, help="Este campo es obligatorio", required=True)
arguments.add_argument('PrecioVenta', type=float,
                       help="Este campo es obligatorio", required=True)
arguments.add_argument('Existencia', type=int,
                       help="Este campo es obligatorio", required=True)
arguments.add_argument('Descripcion', type=str,
                       help="Este campo es obligatorio", required=True)
arguments.add_argument('IdAlmacenista', type=int,
                       help="Este campo es obligatorio", required=True)


api.add_resource(ItemResource, "/middleware/tienda/articulos/")


class ItemResourceDetail(Resource):
    def get(self, id):
        db = DataBase()
        response = db.select_detail("Articulos", "IdArticulo", id)
        return response, 200

    def patch(self, id):
        args = arguments_update.parse_args()
        db = DataBase()
        response = db.update_element("Articulos", "IdArticulo", id, **args)
        return response, 200

    def delete(self, id):
        db = DataBase()
        response = db.delete_element("Articulos", "IdArticulo", id)
        return response, 200


arguments_update = reqparse.RequestParser()
arguments_update.add_argument('IdCategoriadearticulo', type=int,
                              help="Este campo es obligatorio", required=False)
arguments_update.add_argument(
    'Nombre', type=str, help="Este campo es obligatorio", required=False)
arguments_update.add_argument(
    'Marca', type=str, help="Este campo es obligatorio", required=False)
arguments_update.add_argument('PrecioVenta', type=float,
                              help="Este campo es obligatorio", required=False)
arguments_update.add_argument('Existencia', type=int,
                              help="Este campo es obligatorio", required=False)
arguments_update.add_argument('Descripcion', type=str,
                              help="Este campo es obligatorio", required=False)
arguments_update.add_argument('IdAlmacenista', type=int,
                              help="Este campo es obligatorio", required=False)

api.add_resource(ItemResourceDetail, "/middleware/tienda/articulos/<int:id>/")
