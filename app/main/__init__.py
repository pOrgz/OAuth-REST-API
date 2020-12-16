# -*- encoding: utf-8 -*-

"""Initialization of Flask REST-API Environment"""

from flask import Flask
from flask_bcrypt import Bcrypt # Bcrypt hashing for Flask
from flask_sqlalchemy import SQLAlchemy

from .config import config_by_name

db = SQLAlchemy()       # database object
flask_bcrypt = Bcrypt() # bcrypt hashing utilities


def create_app(config_name : str = 'dev'):
    """Initializes the Flask API, by Creating an APP
    with the necessary configurations and parameters which are taken from
    `config`. By default, the environment is intialized, however a
    template `.env` file is present in the `template` branch.

    :type  config_name: str
    :param config_name: Configuration for Setting up the Environment, can be
                        any of the following: ['dev', 'test', 'prod'].
                        Defaults to test, which is mentioned to safekeep
                        production and development environment.
    """
    
    app = Flask(__name__)
    app.config.from_object(config_by_name[config_name])
    db.init_app(app)
    flask_bcrypt.init_app(app)

    return app