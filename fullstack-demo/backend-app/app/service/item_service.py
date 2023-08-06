from app.model.item_model import Item
from app.extensions import db

def save_new_item(data):
    new_item = Item(
        nome = data['nome'],
        preco = data['preco'],
        tempo = data['tempo'],
        categoria = data['categoria'],
        id_user = data['id_user']
    )
    db.session.add(new_item)
    db.session.commit()
    return { "id": new_item.id }

def get_all_items():
    return Item.query.all()

def update_an_item(id_item, data):
    item = Item.query.filter_by(id=id_item).first()
    item.nome = data['nome']
    item.preco = data['preco']
    item.categoria = data['categoria']
    item.tempo = data['tempo']
    db.session.add(item)
    db.session.commit()
    return { "id": item.id }

def delete_by_id(id_item):
    item = Item.query.get(id_item)
    db.session.delete(item)
    db.session.commit()
    return { "id": item.id }