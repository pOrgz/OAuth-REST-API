# -*- encoding: utf-8 -*-

from .. import db

class RolesMaster(db.Model):
    __tablename__ = "roles_master"

    role_id   = db.Column(db.String(64), primary_key = True, nullable = False)
    user_id   = db.Column(db.String(64), db.ForeignKey('users_master.uuid'), nullable = False)
    role_name = db.Column(db.String(32), nullable = False)

    def __repr__(self):
        return f"<{self.role_id}(Role Name = {self.role_name})>"