import sys

sys.path.append('..')

from fastapi import Depends, HTTPException, status, APIRouter
from sqlalchemy.orm import Session

from fastapi_pagination import Page, paginate

from database import engine, get_db
from schemas.user import UserIn, UserOut

from routers.dependencies import get_current_user, get_user_exception
from utils.password import  get_password_hash
from constants import SOMETHING_WENT_WRONG

import models

models.Base.metadata.create_all(bind=engine)
router = APIRouter()


@router.get('/', response_model=Page[UserOut], status_code=status.HTTP_200_OK)
async def get_users(db: Session = Depends(get_db)):
    """
    Get users
    """
    try:
        users =  db.query(models.Users).all()
        return paginate(users)
    except:
        raise HTTPException(status_code=500, detail=SOMETHING_WENT_WRONG)

@router.post('/', status_code=status.HTTP_201_CREATED)
async def create_new_user(create_user: UserIn,
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
            'message': 'User created successfully'
        }
    except:
        raise HTTPException(status_code=400, detail='Username already exists')
