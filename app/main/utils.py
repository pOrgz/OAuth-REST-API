# -*- encoding: utf-8 -*-

"""Password Security with MD5"""

import os
import hashlib

# setting the environment
from dotenv import load_dotenv # Python 3.6+
load_dotenv(verbose = True)

def encrypt(_password : str) -> str:
    """Encrypts the Password with MD5 and SALT"""
    __password_salt__ = os.getenv('forward_salt') + _password + os.getenv('backward_salt')
    return hashlib.sha256(__password_salt__.encode()).hexdigest()

def validate(_password : str, _original_password : str) -> bool:
    """Validate Password"""
    __password_salt__ = os.getenv('forward_salt') + _password + os.getenv('backward_salt')
    
    if hashlib.sha256(__password_salt__.encode()).hexdigest() == _original_password:
        return True

    return False