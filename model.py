from config import *

class Comida(db.Entity):
    nome = Required(str)
    marca = Required(str)
    valor = Optional(str)
    validade = Optional (str)
    def __str__(self):
        return f'{self.nome}, {self.marca}, {self.valor}, {self.validade}'

db.bind(provider='sqlite', filename='comida.db', create_db=True)
db.generate_mapping(create_tables=True)
