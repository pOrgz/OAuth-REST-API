# -*- encoding: utf-8 -*-

from .. import db

class UsersMaster(db.Model):
    __tablename__ = "users_master"

    uuid  = db.Column(db.String(64), primary_key = True, nullable = False) # User ID : generate with UUID-4
    fName = db.Column(db.String(255), nullable = False)                     # First Name
    lName = db.Column(db.String(255), nullable = False)                     # Last/Surname
    email = db.Column(db.String(255), nullable = True)                      # Email ID (optional)
    phone = db.Column(db.String(64), nullable = True)                       # Mobile No. (optional)
    uName = db.Column(db.String(64), primary_key = True, nullable = False, unique = True)
    pHash = db.Column(db.String(128), nullable = False)

    def __repr__(self):
        return f"<{self.uuid}(First Name = {self.fName}, Last Name = {self.lName}, Username = {self.uName})>"