import sys

sys.path.append('..')

from fastapi import Depends, HTTPException, status, APIRouter
from sqlalchemy.orm import Session

from fastapi_pagination import Page, paginate

from database import engine, get_db
from schemas.user import User

from routers.dependencies import get_current_user, get_user_exception
from utils.password import  get_password_hash
from constants import SOMETHING_WENT_WRONG

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
