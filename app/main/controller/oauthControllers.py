# -*- encoding: utf-8 -*-

import time
from flask import request
from flask_restful import Resource, reqparse

from ..models import *
from ..repository import *
from ..utils import validate

class OAuthController(Resource):
    def __init__(self):
        self.oauthRepository = OAuthRepository()

        # Parse Incoming Data arguments for POST
        self.req_parser = reqparse.RequestParser()

        # set arguments i.e. the fields (required from User)
        self.req_parser.add_argument("first_name", type = str, required = False,
            help = "missing, provide First Name of User")
        self.req_parser.add_argument("last_name", type = str, required = False,
            help = "missing, provide Last/Family Name of User")
        self.req_parser.add_argument("email", type = str, required = False)
        self.req_parser.add_argument("phone", type = str, required = False)
        self.req_parser.add_argument("username", type = str, required = False,
            help = "missing, provide Login Username")
        self.req_parser.add_argument("password", type = str, required = False,
            help = "missing, provide Password for Login")
        self.req_parser.add_argument("user_role", type = str, required = False,
            help = "missing, provide User Role like [ADMIN, MANAGER, USER], etc.")

    def post(self):
        """POST Request for User Authentication (login and signup)"""

        args = self.req_parser.parse_args()

        if request.endpoint == "default": # this is sign-up endpoint
            data_message = self.oauthRepository._POST_(args)

            if data_message["status"] == "success":
                _message_body  = "New User Created Sucessfully"
                _error_message = "False"
            else:
                _message_body  = "Unable to Create a New User"
                _error_message = "True"

            return {
                "status" : {
                    "type"    : "signup",
                    "message" : _message_body,
                    "code"    : 200,
                    "error"   : _error_message
                },
                "data" : data_message,
                "time" : str(time.ctime())
            }, 200