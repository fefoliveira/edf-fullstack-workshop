from app import db

class User(db.Model):
    __tablename__ = "user"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)    #primary_key == id principal  //  autoincrement = gera o id sozinho;
    nome = db.Column(db.String(255), nullable=False)                    #nullable == se é ou não indispensável ter essa coluna;
    cpf = db.Column(db.Integer, unique=True, nullable=False)            #unique == nao pode ter nenhum cpf igual.
    endereco = db.Column(db.String(255), nullable=False)   

    items = db.relationship('Item', back_populates='user', uselist=True)
    #db.relationship == relaciona duas classes em um banco de dados relacional, geralmente entre uma classe pai (ou tabela principal) e uma classe filha (ou tabela secundária);
    #back_populates == define o nome que vai ser usado para referenciar a coluna da classe pai na classe filha;
    #uselist == define se essa coluna tem relação com varias outras ou com uma só.

def __init__(self, nome, cpf, endereco):
    self.nome = nome
    self.cpf = cpf
    self.endereco = endereco
        
def __repr__(self):
    return f"<User: '{self.nome}'>"