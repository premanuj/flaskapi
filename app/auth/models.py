from app import db


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key = True, autoincrement=True)
    name = db.Column(db.String(50), nullable= False)
    address = db.Column(db.String(50), nullable = False)

    def __init__(self, name, address):
        self.name = name
        self.address = address
    
    def show(self):
        db.session.query.all()


    def save(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
