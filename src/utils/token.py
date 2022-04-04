from datetime import timedelta, datetime
from typing import Optional
from jose import jwt

from fastapi import HTTPException, status
from config import settings


SECRET_KEY = settings.secret_key
ALGORITHM = settings.algorithm


def create_access_token(username: str,
                        user_id: int,
                        expires_delta: Optional[timedelta] = None):
    """
    Gegenerate JWT token
    Returns:
        Str: Jwt token
    """
    encode = {
        'sub': username,
        'id': user_id
    }

    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)

    encode.update({'exp': expire})
    return jwt.encode(encode, SECRET_KEY, algorithm=ALGORITHM)


def token_exception():
    token_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail='Could not validate token, incorrect token, username or '
               'password',
        headers={'WWW-Authenticate': 'Bearer'},
    )
    return token_exception
