from app import db
from datetime import datetime



class Category(db.Model):
    __tablename__ = 'categories'

    id = db.Column(db.Integer,primary_key = True, autoincrement =True)
    category_name = db.Column(db.String())

    def save_category(self):
        db.session.add(self)
        db.session.commit()  

    def __repr__(self):
        return f'User {self.name}'