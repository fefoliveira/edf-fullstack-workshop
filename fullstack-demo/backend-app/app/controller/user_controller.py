from flask import request
from flask_restx import Resource

from app.util.dto import UserDto
from app.service.user_service import save_new_user, get_all_users, update_an_user, delete_by_id

api = UserDto.api
_user = UserDto.user

@api.route('/')
class User(Resource):
    def post(self):
        data = request.json
        return save_new_user(data)

    @api.marshal_list_with(_user, envelope='data')
    def get(self):
        return get_all_users()

@api.route('/<id_user>')
@api.param('id_user', 'id do vendedor')
class User_with_id(Resource):
    def put(self, id_user):
        data = request.json
        return update_an_user(id_user, data)

    def delete(self, id_user):
        return delete_by_id(id_user)