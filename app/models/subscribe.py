from app import db
from datetime import datetime


class Subscribe(db.Model):

    __tablename__ = 'subscribers'
    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    email = db.Column(db.String())
    timestamp = db.Column(db.DateTime, default=datetime.now())
