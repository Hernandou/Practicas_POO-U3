from mod import db
class Ingrediente(db.Model):

    __tablename__ = 'ingrediente'
    id = db.Column(db.Integer, primary_key = True)
    nombre = ''
    cantidad = 0
    unidad = ''
