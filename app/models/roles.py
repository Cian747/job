from app import db
from datetime import datetime


class Role(db.Model):
    __tablename__ = 'roles'

    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(255))
    users = db.relationship('User',backref = 'role',lazy="dynamic")

    def __init__(self, name):
        '''
        Method that defines Category object properties.
        Args: 
            category_name: New category name
        '''
        self.name = name

    def get_roles():
        '''
        Method that retrieves all user roles
        '''
        roles = Role.query.all()
        return roles

    def __repr__(self):
        return f'User {self.name}'
    
    