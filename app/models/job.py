from app import db
from datetime import datetime

class Jobs(db.Model):

    __tablename__ = 'joblistings'

    id = db.Column(db.Integer, primary_key = True)
    job_id = db.Column(db.String(), unique = True)
    commitment = db.Column(db.String())
    department = db.Column(db.String())
    team = db.Column(db.String())
    location = db.Column(db.String())
    descriptionPlain = db.Column(db.String())
    text = db.Column(db.String())
    applyUrl = db.Column(db.String())
    posted_by = db.Column(db.Integer,db.ForeignKey('users.id'))

class Jobs2:
    def __init__(self, job_id, commitment, department, team, location, descriptionPlain, text, applyUrl):
        
        self.job_id = job_id
        self.commitment = commitment
        self.department= department
        self.team = team
        self.location = location
        self.descriptionPlain = descriptionPlain
        self.text = text
        self.applyUrl = applyUrl


class Jobs3:
    def __init__(self, job_id, category, descriptionPlain, text, applyUrl):
        
        self.job_id = job_id
        self.category = category
        self.descriptionPlain = descriptionPlain
        self.text = text
        self.applyUrl = applyUrl
        




