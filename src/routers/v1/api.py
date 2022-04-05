from fastapi import APIRouter
from routers.v1.endpoints import auth, todos, users


router = APIRouter()

router.include_router(auth.router, prefix="", tags=["Authentication"])
router.include_router(users.router, prefix="/users", tags=["Users"])
router.include_router(todos.router, prefix="/todos", tags=["Todos"])
