import sys

sys.path.append('..')

from fastapi import Depends, HTTPException, status, APIRouter
from fastapi_pagination import Page, paginate
from sqlalchemy.orm import Session

from database import engine, get_db
from schemas.user import User

from routers.dependencies import get_current_user, get_user_exception
from routers.v1.constants import USER_NOT_FOUND

import models

models.Base.metadata.create_all(bind=engine)
router = APIRouter()


@router.get('/', response_model=Page[User], status_code=status.HTTP_200_OK)
async def get_users(db: Session = Depends(get_db)):
    """
    Get users
    """
    users =  db.query(models.Users).all()
    return paginate(users)


@router.get('/me', response_model=User, status_code=status.HTTP_200_OK)
async def get_users(current_user: dict = Depends(get_current_user),
                    db: Session = Depends(get_db)):
    """
    Return information for current user
    """
    return db.query(models.Users)\
        .filter(models.Users.id == current_user['id'])\
        .first()

@router.get('/{user_id}', response_model=User, status_code=status.HTTP_200_OK)
async def get_users(user_id: int,
                    current_user: dict = Depends(get_current_user),
                    db: Session = Depends(get_db)):
    """
    Return information with user id
    """
    if not current_user:
        raise get_user_exception()

    user = db.query(models.Users)\
        .filter(models.Users.id == user_id)\
        .first()

    if user is not None:
        return user

    raise HTTPException(status_code=404, detail=USER_NOT_FOUND)
