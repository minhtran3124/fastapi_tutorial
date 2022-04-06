from datetime import timedelta

from fastapi import Depends, APIRouter, status, HTTPException
from sqlalchemy.orm import Session

from config import settings
from database import engine, get_db
from schemas.user import UserLogin, UserCreate

from utils.password import verify_password, get_password_hash
from utils.token import create_access_token, token_exception

import models

SECRET_KEY = settings.secret_key
ALGORITHM = settings.algorithm

# models.Base.metadata.create_all(bind=engine)

router = APIRouter()


def authenticate_user(db, username: str, password: str):
    """
    Authenticate user based on given username and password
    Args:
        db (Session): Database session
        username (Str): Username
        password (str): Plain text password
    Returns:
        Dict: User data
    """
    user = db.query(models.Users).filter(
        models.Users.username == username).first()

    if not user:
        return False

    if not verify_password(password, user.hashed_password):
        return False

    return user


@router.post('/login')
async def login(auth_user: UserLogin, db: Session = Depends(get_db)):
    """
    OAuth2 compatible token login, get an access token for future requests
    """
    user = authenticate_user(db, auth_user.username, auth_user.password)

    if not user:
        raise token_exception()

    access_token_expires = timedelta(minutes=20)
    access_token = create_access_token(
        user.username, user.id, expires_delta=access_token_expires
    )
    return {
        'access_token': access_token,
        'token_type': 'bearer'
    }

@router.post('/signup', status_code=status.HTTP_201_CREATED)
async def signup(create_user: UserCreate, db: Session = Depends(get_db)):
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
            'message': 'User created successfully'
        }
    except Exception:
        raise HTTPException(status_code=400, detail='Username already exists')
