# -*- encoding: utf-8 -*-

"""API Management and Server Running Module"""

import os
from flask_restful import Api

from app.main import (
        db, # SQLAlchemy Connector dB Object
        create_app
    )

# setting the environment
from dotenv import load_dotenv # Python 3.6+
load_dotenv(verbose = True) # configure .env File or set Environment Variables

app = create_app(os.getenv("PROJECT_ENV_NAME") or "dev") # check config.py
api = Api(app)

### --- List of all Resources --- ###
from app.main.controller import *

if __name__ == "__main__":
    app.run(
        port = os.getenv('port', 5000), # run the application on default 5000 Port
        host = os.getenv('host', 'localhost') # define host, as required
    )