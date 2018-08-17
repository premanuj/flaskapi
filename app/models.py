from app import db

class Provider(db.Model):
    __tablename__ = 'providers'

    id = db.Column(db.Integer, primary_key = True, autoincrement=True)
    name = db.Column(db.String(50), nullable= False)
    name_id = db.Column(db.Integer, nullable = False)