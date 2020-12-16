# -*- encoding: utf-8 -*-

import time
from uuid import uuid1, uuid4
from sqlalchemy.exc import IntegrityError

from .. import db
from ..utils import *
from ..models import *

class OAuthRepository:
    def _POST_(self, json : dict) -> [dict, int]:
        """Repository for handling POST requests"""

        _user_id_ = str(uuid4()) # as defined in models
        _role_id_ = str(uuid1()) # as defined in models

        try:
            # update `users_masters`
            data = UsersMaster(
                    uuid  = _user_id_,
                    fName = json.first_name,
                    lName = json.last_name,
                    email = json.email,
                    phone = json.phone,
                    uName = json.username,
                    pHash = encrypt(json.password)
                )
            db.session.add(data) # add to staging area
            db.session.commit()  # permanently add data to db

            # update `roles_master`
            data = RolesMaster(
                    role_id   = _role_id_,
                    user_id   = _user_id_,
                    role_name = json.user_role
                )
            db.session.add(data) # add to staging area
            db.session.commit()  # permanently add data to db

            # update `logins_master`
            data = LoginsMaster(
                    id         = _user_id_[:7] + _role_id_[:7],
                    user_id    = _user_id_,
                    role_id    = _role_id_,
                    login_time = str(time.ctime())
                )
            db.session.add(data) # add to staging area
            db.session.commit()  # permanently add data to db

            return {
                "status" : "success",
                "user"   : {
                    "user-id"  : f"{_user_id_}",
                    "username" : f"{json.username}",
                    "email"    : f"{json.email}",
                    "fullname" : f"{json.first_name} {json.last_name}"
                },
                "remarks"  : "None",
                "errorMsg" : "None"
            }
        except IntegrityError as err:
            return {
                "status" : "failed",
                "user"   : {
                    "user-id"  : "None",
                    "username" : f"{json.username}",
                    "email"    : f"{json.email}",
                    "fullname" : f"{json.first_name} {json.last_name}"
                },
                "remarks"  : "username must be unique",
                "errorMsg" : str(err)
            }