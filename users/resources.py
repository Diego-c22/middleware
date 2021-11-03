"""Resources to connect to Users and TipodeUsuarios Models"""

from flask import Blueprint
from db.db import DataBase
from flask_restful import Resource, Api, abort, reqparse

users_v1 = Blueprint("users_v1", __name__)
api = Api(users_v1)


class UsersResource(Resource):
    def get(self, table):
        db = DataBase()
        response = db.select_all(table)
        return response, 200

    def post(self, table):

        if table == "tipodeusuarios":
            abort(401, message="No tiene autorizacion para agregar ese elemento")
        if table == "usuarios":
            args = arguments.parse_args()
            db = DataBase()
            print("im inside")
            r = db.insert_element(table, "IdUsuario", **args)

            return r
        abort(404)


arguments = reqparse.RequestParser()
arguments.add_argument(
    "Nombre", type=str, help="Este campo es obligatorio", required=True
)
arguments.add_argument(
    "Apellido", type=str, help="Este campo es obligatorio", required=True
)
arguments.add_argument(
    "Correo", type=str, help="Este campo es obligatorio", required=True
)
arguments.add_argument(
    "NombreUsuario", type=str, help="Este campo es obligatorio", required=True
)
arguments.add_argument(
    "Contrasena", type=str, help="Este campo es obligatorio", required=True
)
arguments.add_argument(
    "Imagen", type=str, help="Este campo es obligatorio", required=True
)
arguments.add_argument(
    "IdTipoUsuario", type=int, help="Este campo es obligatorio", required=True
)
api.add_resource(UsersResource, "/middleware/usuario/<string:table>/")


class UsersResourceDetail(Resource):
    def get(self, table, id):
        db = DataBase()
        if table == "usuarios":
            response = db.select_detail(table, "idusuario", id)
            return response, 200

        if table == "tipodeusuarios":
            response = db.select_detail(table, "idtipousuario", id)
            return response, 200

        abort(404, message="No se encontro el elemento")

    def patch(self, table, id):

        if table == "tipodeusuarios":
            abort(401, message="No tiene autorizacion para actualizar ese elemento")
        if table == "usuarios":
            args = arguments_update.parse_args()
            db = DataBase()
            r = db.update_element(table, "IdUsuario", id, **args)

            return r

        abort(404)

    def delete(self, table, id):
        if table == "tipodeusuarios":
            abort(401, message="No tiene autorizacion para eliminar ese elemento")
        if table == "usuarios":
            db = DataBase()
            print("im inside")
            r = db.delete_element(table, "IdUsuario", id)

            return r
        abort(404)


arguments_update = reqparse.RequestParser()
arguments_update.add_argument(
    "Nombre", type=str, help="Este campo es obligatorio", required=False
)
arguments_update.add_argument(
    "Apellido", type=str, help="Este campo es obligatorio", required=False
)
arguments_update.add_argument(
    "Correo", type=str, help="Este campo es obligatorio", required=False
)
arguments_update.add_argument(
    "NombreUsuario", type=str, help="Este campo es obligatorio", required=False
)
arguments_update.add_argument(
    "Contrasena", type=str, help="Este campo es obligatorio", required=False
)
arguments_update.add_argument(
    "Imagen", type=str, help="Este campo es obligatorio", required=False
)
arguments_update.add_argument(
    "IdTipoUsuario", type=int, help="Este campo es obligatorio", required=False
)
api.add_resource(UsersResourceDetail,
                 "/middleware/usuario/<string:table>/<int:id>/")


class UsersNameResourceDetail(Resource):
    def get(self, username):
        db = DataBase()
        response = db.select_detail("usuarios", "NombreUsuario", username)
        return response, 200


api.add_resource(UsersNameResourceDetail,
                 "/middleware/usuario/usuarios/u/<string:username>/")
