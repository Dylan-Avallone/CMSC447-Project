# SQLbackend/auth.py
from data import users

def authenticate(email: str, password: str) -> bool:
    """
    Return True if credentials match, else False
    """
    return users.get(email) == password