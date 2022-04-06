from fastapi import Request, status
from fastapi.exceptions import RequestValidationError
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

from constants import SOMETHING_WENT_WRONG


class UnicornException(Exception):
    def __init__(self, name: str):
        self.name = name


# Custom data validation error
async def validation_exception_handler(
    request: Request, exc: RequestValidationError
) -> JSONResponse:
    detail = []
    for error in exc.errors():
        detail.append({
            'field': error['loc'][1],
            'msg': error['msg']
        })

    return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST,
                        content=jsonable_encoder(detail))


# Uncontrolled internal server errors (e.g. raised by FastAPI's middlewares)
async def internal_error_exception_handler(
    request: Request, exc: RequestValidationError
) -> JSONResponse:
    return JSONResponse(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                        content=jsonable_encoder({'detail': SOMETHING_WENT_WRONG}))
