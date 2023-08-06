from app.model.user_model import User
from app.extensions import db

def save_new_user(data):
    new_user = User(
        nome = data['nome'],
        cpf = data['cpf'],
        endereco = data['endereco'],
    )
    db.session.add(new_user)
    db.session.commit()
    return { "id": new_user.id }

def get_all_users():
    return User.query.all()

def update_an_user(id_user, data):
    user = User.query.filter_by(id=id_user).first()
    user.nome = data['nome']
    user.cpf = data['cpf']
    user.endereco = data['endereco']
    db.session.add(user)
    db.session.commit()
    return { "id": user.id }

def delete_by_id(id_user):
    user = User.query.get(id_user)
    db.session.delete(user)
    db.session.commit()
    return { "id": user.id }