from utils.db import db
from dataclasses import dataclass

@dataclass
class Contact(db.Model):
    id: int
    fullname: str
    email: str
    phone: str
    
    #Correspondencia con DB
    id = db.Column(db.Integer, primary_key = True)
    fullname = db.Column(db.String(100))
    email = db.Column(db.String(60))
    phone = db.Column(db.String(20))

    def __init__(self, fullname, email,phone):
        self.fullname = fullname
        self.email = email
        self.phone = phone