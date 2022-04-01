from fastapi import APIRouter
from routers import auth, todos


router = APIRouter()

router.include_router(auth.router, prefix="/users", tags=["Users"])
router.include_router(todos.router, prefix="/todos", tags=["Todos"])
