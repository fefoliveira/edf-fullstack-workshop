from flask_restx import Namespace, fields

class UserDto:
    api = Namespace('user', description='user related operations')
    user = api.model('user', {
        'nome': fields.String(required=True, description='user name'),
        'cpf': fields.Integer(required=True, description='user cpf'),
        'endereco': fields.String(required=True, description='user address'),
    })

class ItemDto:
    api = Namespace('items', description='items related operations')
    items = api.model('items', {
        'nome': fields.String(required=True, description='item name'),
        'preco': fields.Integer(required=True, description='item price'),
        'categoria': fields.String(required=True, description='item category'),
        'tempo': fields.Integer(required=True, description='item age'),
        'id_user': fields.Integer(required=True, description='item seller'),
    })