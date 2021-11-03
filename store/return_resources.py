"""Resources to connect to Devoluciones model"""
from flask import Blueprint
from db.db import DataBase
from flask_restful import Resource, Api, abort, reqparse

return_v1 = Blueprint("return_v1", __name__)
api = Api(return_v1)


class ReturnResource(Resource):
    def get(self):
        try:
            db = DataBase()
            response = db.select_all("Devoluciones")
            print(response)
            return response, 200
        except Exception as e:
            raise e
            abort(404, message="No se encontraron elementos")

    def post(self):
        args = arguments.parse_args()
        db = DataBase()
        response = db.insert_element("Devoluciones", "IdDevolucion", ** args)
        print(response)
        return response, 200


arguments = reqparse.RequestParser()
arguments.add_argument('FechaDevolucion', type=str,
                       help="Este campo es obligatorio", required=True)
arguments.add_argument(
    'IdArticuloComprado', type=int, help="Este campo es obligatorio", required=True)


api.add_resource(ReturnResource, "/middleware/tienda/devoluciones/")


class ReturnResourceDetail(Resource):
    def get(self, id):
        db = DataBase()
        response = db.select_detail("Devoluciones", "IdDevolucion", id)
        return response, 200

    def patch(self, id):
        args = arguments_update.parse_args()
        db = DataBase()
        response = db.update_element(
            "Devoluciones", "IdDevolucion", id, **args)
        return response, 200

    def delete(self, id):
        db = DataBase()
        response = db.delete_element("Devoluciones", "IdDevolucion", id)
        return response, 200


arguments_update = reqparse.RequestParser()
arguments_update.add_argument('FechaDevolucion', type=str,
                              help="Este campo es obligatorio", required=False)
arguments_update.add_argument(
    'IdArticuloComprado', type=int, help="Este campo es obligatorio", required=False)


api.add_resource(ReturnResourceDetail,
                 "/middleware/tienda/devoluciones/<int:id>")
