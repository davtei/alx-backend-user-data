#!/usr/bin/env python3

""" Encrypting user passwords """
import bcrypt
from bcrypt import hashpw


def hash_password(password: str) -> bytes:
    """ Returns a salted, hashed password in bytes string """
    b = password.encode()
    hashed = hashpw(b, bcrypt.gensalt())
    return hashed


def is_valid(hashed_password: bytes, password: str) -> bool:
    """ Validates that the provided password matches the hashed password """
    return bcrypt.checkpw(password.encode(), hashed_password)
