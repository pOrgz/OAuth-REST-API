# -*- encoding: utf-8 -*-

from .. import db

class LoginsMaster(db.Model):
    __tablename__ = "logins_master"

    id         = db.Column(db.String(64), primary_key = True, nullable = False) # login ID
    user_id    = db.Column(db.String(64), db.ForeignKey('users_master.uuid'), nullable = False)
    role_id    = db.Column(db.String(64), db.ForeignKey('roles_master.role_id'), nullable = False)
    login_time = db.Column(db.String(64), nullable = True)

    def __repr__(self):
        return f"<{self.id}(Login Time = {self.login_time})>"