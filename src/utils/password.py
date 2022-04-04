import sys

sys.path.append('..')

from passlib.context import CryptContext

from config import settings


SECRET_KEY = settings.secret_key
ALGORITHM = settings.algorithm

bcrypt_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def get_password_hash(password: str):
    """
    Generate Hash Password from plain password
    Args:
        password (Str): Plain text
    Returns:
        [Str]: Hash password
    """
    return bcrypt_context.hash(password)


def verify_password(plain_password: str, hashed_password: str):
    """
    Verify password from plain text
    Args:
        plain_password (Str): Plain text
        hashed_password (Str): Hash password
    Returns:
        Bool: True or False
    """
    return bcrypt_context.verify(plain_password, hashed_password)
