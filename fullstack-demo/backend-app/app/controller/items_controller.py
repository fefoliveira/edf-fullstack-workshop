from flask import request
from flask_restx import Resource

from app.util.dto import ItemDto
from app.service.item_service import save_new_item, get_all_items, update_an_item, delete_by_id

api = ItemDto.api
_items = ItemDto.items

@api.route('/')
class Item(Resource):
    def post(self):
        data = request.json
        return save_new_item(data)

    @api.marshal_list_with(_items, envelope='data')
    def get(self):
        return get_all_items()


@api.route('/<id_item>')
@api.param('id_item', 'id do produto')
class Item_with_id(Resource):
    def put(self, id_item):
        data = request.json
        return update_an_item(id_item, data)

    def delete(self, id_item):
        return delete_by_id(id_item)