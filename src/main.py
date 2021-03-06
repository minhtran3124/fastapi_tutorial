import uvicorn

from fastapi import FastAPI, Request
from fastapi.exceptions import RequestValidationError, ValidationError
from fastapi.responses import JSONResponse

from sqladmin import Admin
from fastapi_pagination import add_pagination

from base.custom_exceptions import (
    validation_exception_handler,
    internal_error_exception_handler
)
from constants import API_V1
from admins import TodoAdmin, UserAdmin
from database import engine
from config import settings
from routers.v1.api import router as api_router

import models


models.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Todo",
    exception_handlers = {
        500: internal_error_exception_handler,
        RequestValidationError: validation_exception_handler
    }
)


# Include API router for application
app.include_router(api_router, prefix=API_V1)


# Initialize admin and register models
admin = Admin(app, engine)
admin.register_model(UserAdmin)
admin.register_model(TodoAdmin)


# # Config for custom handle exception
# @app.exception_handler(RequestValidationError)
# @app.exception_handler(ValidationError)
# async def custom_validation_exception_handler(
#     request: Request, exc: RequestValidationError
# ) -> JSONResponse:
#     return await validation_exception_handler(request, exc)


# Add pagination for applcation
add_pagination(app)


if __name__ == '__main__':
    uvicorn.run('__main__:app',
                host=settings.host,
                port=settings.port,
                reload=True,
                workers=2
            )
