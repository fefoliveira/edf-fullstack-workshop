from app import db

class Item(db.Model):
    __tablename__ = "item"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)    #primary_key == id principal  //  autoincrement = gera o id sozinho;
    nome = db.Column(db.String(255), nullable=False)                    #nullable == se é ou não indispensável ter essa coluna;
    preco = db.Column(db.Integer, nullable=False)   
    categoria = db.Column(db.String(255), nullable=False)
    tempo = db.Column(db.Integer)
    
    id_user = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)    
    #db.foreign_keys('user.id) == especifica que a coluna 'id_user' (coluna desta tabela) é uma chave estrangeira que faz referência à coluna 'id' na tabela 'user'.
    user = db.relationship('User', foreign_keys=[id_user], back_populates='items', uselist=False)
    #db.relationship == relaciona duas classes em um banco de dados relacional, geralmente entre uma classe pai (ou tabela principal) e uma classe filha (ou tabela secundária);
    #foreign_keys == define as colunas que podem fazer parte do relacionamento (mostra qual a chave estrangeira que está sendo usada pra essa relação);
    #back_populates == define o nome que vai ser usado para referenciar a coluna da classe pai na classe filha;
    #uselist == define se essa coluna tem relação com varias outras ou com uma só.

def __init__(self, nome, preco, categoria, tempo, id_user):
    self.nome = nome
    self.preco = preco
    self.categoria = categoria
    self.tempo = tempo
    self.id_user = id_user
        
def __repr__(self):
    return f"<Item: '{self.nome}'>"