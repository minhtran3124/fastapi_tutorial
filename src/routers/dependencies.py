from jose import jwt, JWTError

from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer

from config import settings
from routers.v1.constants import UNAUTHORIZED_ERROR_MESSAGE

SECRET_KEY = settings.secret_key
ALGORITHM = settings.algorithm


oauth_bearer = OAuth2PasswordBearer(tokenUrl='token')


async def get_current_user(token: str = Depends(oauth_bearer)):
    """
    Get the user details from the JWT token
    Args:
        token (str, optional): [description]. Defaults to Depends(oauth_bearer).
    Raises:
        HTTPException: If user details not found in token
        HTTPException: If token is not valid
    Returns:
        str: User details
    """
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get('sub')
        user_id: int = payload.get('id')

        if username is None or user_id is None:
            raise get_user_exception()

        return {
            'id': user_id,
            'username': username
        }
    except JWTError:
        raise get_user_exception()


def get_user_exception():
    """
    Raise credential exception if token is not validated
    """
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail=UNAUTHORIZED_ERROR_MESSAGE,
        headers={'WWW-Authenticate': 'Bearer'},
    )
    return credentials_exception
