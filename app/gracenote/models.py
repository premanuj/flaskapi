from app import db


class Provider(db.Model):
    __tablename__ = 'providers'

    id = db.Column(db.Integer, primary_key = True, autoincrement=True)
    name = db.Column(db.String(50), nullable= False)
    name_ids = db.Column(db.Integer, nullable = False)

    def __init__(self, name, name_id):
        # self.id = id
        self.name = name
        self.name_ids = name_id
    
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
