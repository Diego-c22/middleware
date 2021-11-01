from flask import Blueprint
from flask_restful import Api, Resource, abort, reqparse

users_v1 = Blueprint("users_v1", __name__)
api = Api(users_v1)


class UsersResource(Resource):
    pass
