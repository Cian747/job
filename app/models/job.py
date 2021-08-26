from app import db
from datetime import datetime

class Jobs(db.Model):

    __tablename__ = 'joblistings'

    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    job_id = db.Column(db.String(), unique = True)
    commitment = db.Column(db.String())
    department = db.Column(db.String())
    team = db.Column(db.String())
    location = db.Column(db.String())
    descriptionPlain = db.Column(db.String())
    text = db.Column(db.String())
    applyUrl = db.Column(db.String())
    posted_by = db.Column(db.Integer,db.ForeignKey('users.id'))

    def get_joblistings(user_id):
        listing = Jobs.query.filter_by(posted_by=user_id).order_by(Jobs.id.desc()).all()
        return listing



class Jobs(db.Model):
    __tablename__ = 'joblistings'

    id = db.Column(db.Integer, primary_key=True, autoincrement = True)
    job_id = db.Column(db.String())
    commitment = db.Column(db.String())
    department = db.Column(db.String())
    team = db.Column(db.String())
    location = db.Column(db.String())
    descriptionPlain = db.Column(db.String())
    text = db.Column(db.String())
    applyUrl = db.Column(db.String())
    posted_by = db.Column(db.Integer,db.ForeignKey('users.id'))
