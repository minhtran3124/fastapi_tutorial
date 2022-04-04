import sys

sys.path.append('..')

from jose import jwt, JWTError

from fastapi import Depends, HTTPException, status, APIRouter
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session

from config import settings
from database import SessionLocal, engine, get_db
from schemas.user import CreateUser

from utils.password import  get_password_hash
from utils.token import create_access_token, token_exception

import models

SECRET_KEY = settings.secret_key
ALGORITHM = settings.algorithm


models.Base.metadata.create_all(bind=engine)

oauth_bearer = OAuth2PasswordBearer(tokenUrl="token")

router = APIRouter()


@router.post('/', status_code=status.HTTP_201_CREATED)
async def create_new_user(create_user: CreateUser,
                          db: Session = Depends(get_db)):
    """
    Create a new user
    """
    try:
        create_user_model = models.Users()
        create_user_model.username = create_user.username
        create_user_model.email = create_user.email
        create_user_model.first_name = create_user.first_name
        create_user_model.last_name = create_user.last_name

        hash_password = get_password_hash(create_user.password)
        create_user_model.hashed_password = hash_password
        create_user_model.is_active = True

        db.add(create_user_model)
        db.commit()

        return {
            "message": "User created successfully"
        }
    except:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail='Username already exists')


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
            'username': username,
            'id': user_id
        }
    except JWTError:
        raise get_user_exception()


# Exceptions
def get_user_exception():
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail='Could not validate credentials',
        headers={'WWW-Authenticate': 'Bearer'},
    )
    return credentials_exception
