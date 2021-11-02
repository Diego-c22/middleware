from flask import Blueprint
from db.db import DataBase
from flask_restful import Resource, Api, abort, reqparse

items_v1 = Blueprint("items_v1", __name__)
api = Api(items_v1)


class ItemResource(Resource):
    def get(self):
        try:
            db = DataBase()
            response = db.select_all("Articulos")
            print(response)
            return response, 200
        except Exception as e:
            raise e
            abort(404, message="No se encontraron elementos")


api.add_resource(ItemResource, "/middleware/tienda/articulos/")
